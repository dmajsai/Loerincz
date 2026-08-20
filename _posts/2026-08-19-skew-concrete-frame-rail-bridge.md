---
title: "Skew concrete frame rail bridges: why the angle changes the analysis"
description: >-
  Design and analysis of oblique-angled reinforced concrete frame structures for
  railway bridges, and how skew geometry redistributes load away from the
  assumptions that hold for square structures.
date: 2026-08-19
cluster: railway-bridges
cluster_name: Railway bridges
client: DB German Rail Network
scope: Design and analysis
structure: Reinforced concrete frame, oblique angled
services: Structural design, structural analysis
image: /images/unnamed-37.png
image_alt: >-
  Plan drawing of a skew railway structure showing the oblique crossing angle
  between the structure and the track alignment
image_caption: >-
  Plan of the skew crossing. The angle between the structure and the alignment it
  carries is what drives the analysis.
---

A skew bridge is one where the structure does not cross what it spans at a right
angle. In English the term is skew; in German drawings it appears as an
oblique-angled or *schiefwinklig* structure. The distinction matters because the
behaviour of a skew frame differs from a square one in ways that are easy to
underestimate.

We have carried out design and analysis of oblique-angled concrete frame
structures for railway bridges in the DB German Rail network, on more than one
occasion.

## Why the angle is not a detail

Skew is rarely chosen. It is imposed by whatever the structure crosses, since
roads, watercourses and other railways run where they run. Once the angle is
below roughly seventy degrees, a set of effects appear that a square-structure
analysis does not capture.

**Load does not travel the way the span suggests.** In a skew slab or frame, load
takes the shortest stiff path to the supports rather than running parallel to the
free edges. The effective span is shorter than the measured one, and the load
concentrates along the line connecting the obtuse corners.

**The obtuse corners attract reaction.** Support reactions are not distributed
evenly along the abutment. They concentrate sharply at the obtuse corners, and
the higher the skew, the sharper the concentration.

**The acute corners can lift.** As reaction concentrates at the obtuse corners,
the acute corners shed load and can go into uplift. A bearing designed only for
compression is then in the wrong condition, and the structure has to be checked
for whether hold-down is required.

**Twisting moments become significant.** Skew slabs carry a substantial part of
the load in torsion. Principal moments rotate away from the span direction, which
means reinforcement laid out on the span axis is no longer aligned with the way
the structure actually wants to carry load.

## What this requires of the analysis

Skew geometry rules out simplified strip methods. The structure has to be modelled
as a plate or shell so the twisting moments and the corner effects appear in the
results rather than being smoothed away.

The reinforcement then has to be resolved from the principal moment field. Bars
are practical to place either parallel to the free edge or parallel to the
support line, and neither direction matches the principal moments across the whole
deck. The design has to convert the principal moments into resistance in the
directions the bars actually run, which is what governs the layout in the corner
regions.

Corner detailing carries a disproportionate share of the design effort. The obtuse
corners need reinforcement against the concentrated reaction and the local hogging
that develops there, and this is the region where skew structures show distress if
the effect has been underestimated.

## Frame structures specifically

For a frame rather than a simply supported deck, the walls and the deck act
together. The skew angle carries through the whole frame, so the connection
between deck and walls has to transfer moment across a joint that is itself
oblique. Continuity between the elements changes both how load distributes and
how the structure responds to settlement and temperature.

Earth pressure on the walls has to be considered alongside the structural loading,
and for a rail structure the surcharge from the track and its loading is part of
that. Geotechnical input and structural analysis are not separable on this kind of
frame.

## Standards and tools

Design and analysis followed the Eurocodes as adopted in Germany, DIN EN 1990
through 1998, including the sections covering concrete design and actions on
structures from rail traffic. Finite element modelling used SOFiSTiK, Dlubal and
RFEM, with GGU used for geotechnical checks on the frame walls and foundations.

The deliverable is a static analysis document covering the model, the load cases,
the reinforcement design and the corner detailing, in a form suitable for
approval.
