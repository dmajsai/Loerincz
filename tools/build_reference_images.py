#!/usr/bin/env python3
"""Build full-size and thumbnail WebP files for the project references."""

import argparse
import json
import re
import subprocess
from pathlib import Path


DEFAULT_SOURCE = Path(
    "/private/tmp/claude-501/-Users-majsai-Projects/"
    "c2db498e-afd0-4790-a351-734a2d13d6e8/scratchpad/"
    "docx/x/word/media"
)


def dimensions_from_sips(path):
    result = subprocess.run(
        ["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    width = re.search(r"pixelWidth: (\d+)", result.stdout)
    height = re.search(r"pixelHeight: (\d+)", result.stdout)
    if not width or not height:
        raise RuntimeError(f"Could not read source dimensions: {path}")
    return int(width.group(1)), int(height.group(1))


def dimensions_from_webpinfo(path):
    result = subprocess.run(
        ["webpinfo", str(path)], check=True, capture_output=True, text=True
    )
    width = re.search(r"Width:\s*(\d+)", result.stdout)
    height = re.search(r"Height:\s*(\d+)", result.stdout)
    if not width or not height:
        raise RuntimeError(f"Could not read WebP dimensions: {path}")
    return int(width.group(1)), int(height.group(1))


def encode(source, output, source_width, max_width, quality):
    command = ["cwebp", "-q", str(quality), "-m", "6"]
    if source_width > max_width:
        command.extend(["-resize", str(max_width), "0"])
    command.extend([str(source), "-o", str(output)])
    subprocess.run(command, check=True)
    return dimensions_from_webpinfo(output)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_dir", nargs="?", type=Path, default=DEFAULT_SOURCE)
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    data_path = root / "_data" / "references.yml"
    ruby = (
        "require 'yaml'; require 'json'; "
        "puts JSON.generate(YAML.load_file(ARGV.fetch(0)))"
    )
    data_json = subprocess.run(
        ["ruby", "-e", ruby, str(data_path)],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    references = json.loads(data_json)

    output_dir = root / "images" / "references"
    output_dir.mkdir(parents=True, exist_ok=True)
    sizes = {}

    for reference in references:
        for image in reference.get("images", []):
            name = image["file"]
            source = args.source_dir / f"image{image['src']}.png"
            source_width, _ = dimensions_from_sips(source)
            full = output_dir / f"{name}.webp"
            thumb = output_dir / f"{name}-thumb.webp"
            width, height = encode(source, full, source_width, 1400, 88)
            thumb_width, thumb_height = encode(source, thumb, source_width, 640, 85)
            sizes[name] = {
                "w": width,
                "h": height,
                "tw": thumb_width,
                "th": thumb_height,
            }

    lines = []
    for name, dimensions in sizes.items():
        lines.append(f"{name}:")
        for key in ("w", "h", "tw", "th"):
            lines.append(f"  {key}: {dimensions[key]}")
    (root / "_data" / "reference_images.yml").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
