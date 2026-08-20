---
title: "Refurbishing a prestressed concrete rail bridge: analysis, new cross-section and reinforcement"
description: >-
  Statical analysis and refurbishment of prestressed concrete railway bridges for
  DB German Rail, covering assessment of the existing structure, cross-section
  upgrade and added reinforcement.
date: 2026-08-20
cluster: railway-bridges
cluster_name: Railway bridges
client: DB German Rail
scope: Statical analysis and refurbishment
structure: Prestressed concrete
services: Structural analysis, static analysis documentation
image: /images/unnamed-25.png
image_alt: >-
  Cross-section drawing of a prestressed concrete railway bridge showing deck
  build-up, bearing detail and structural dimensions
image_caption: >-
  Cross-section through the bridge deck showing the existing structure and the
  levels that governed the refurbishment.
---

Refurbishment starts from a harder position than new design. On a new structure
you choose the geometry and specify the materials. On an existing bridge both are
already fixed, and the first job is finding out what you actually have.

We carried out comprehensive statical analysis for prestressed concrete railway
bridges in the DB German Rail network, including refurbishment with new
cross-sections and added reinforcement.

## Why these bridges need assessing

Germany's rail network carries a large stock of prestressed concrete bridges built
from the 1950s onward. Most are in sound condition. The reason they come up for
assessment is usually not deterioration but change: load models have been revised,
traffic has grown heavier, clearance requirements have tightened, or the line is
being upgraded and the structure has to accommodate something it was never
designed for.

An assessment answers a narrow question. Not "is this bridge adequate" in general,
but "does this bridge satisfy current requirements for the loading it will now
carry". A structure can pass comfortably under the code it was designed to and
still fail against a current load model.

## Establishing the existing capacity

The analysis has to be built on what the structure is, not what the drawings say
it should be. For prestressed concrete that means resolving several unknowns.

**Prestress losses.** Creep, shrinkage and relaxation reduce the effective
prestress over decades. The remaining force is what governs behaviour under
service loads, and it has to be estimated from the age and history of the
structure rather than assumed at the design value.

**Tendon condition and position.** Duct grouting quality and tendon layout affect
both durability and capacity. Where records are incomplete, this needs
investigation rather than assumption.

**Concrete and reinforcement properties.** Actual material strengths often exceed
the specified values, which can work in the assessment's favour, but only if they
are established by testing rather than assumed.

Getting these right matters more than refining the analysis model. A precise
calculation built on an assumed prestress value is a precise calculation of the
wrong structure.

## FEM modelling

Detailed finite element simulation was used to assess structural integrity and
performance under a range of load conditions. For a prestressed deck the model
needs to represent the prestress as an applied action rather than a material
property, capture the construction sequence where it affects the locked-in stress
state, and cover the load cases that govern at different points along the span.

Rail loading adds requirements that road bridge analysis does not have. Dynamic
amplification has to be applied to the static load model, and deflection and end
rotation have to be checked against track geometry limits, not just structural
ones. On refurbishment these serviceability checks frequently govern, because the
existing structure was designed against limits that have since been tightened.

## Cross-section upgrade and reinforcement

The refurbishment included upgrading the bridge's cross-section and adding new
reinforcement to improve durability and safety.

Widening a deck changes more than the deck. Additional width adds permanent load
across the whole span, shifts the load path into the existing bearings and
substructure, and alters how the structure distributes load transversely. The
supporting elements have to be checked against the revised loading even where no
work is planned on them, and it is common for the substructure rather than the
deck to become the limiting element.

Added reinforcement has to be made to work with a structure that is already
carrying load. New reinforcement only takes up force from additional load applied
after it is installed, so it does not relieve the existing stress state. Where
strengthening is needed against permanent load, the structure has to be unloaded
first, or the analysis has to account for the fact that the new material starts
from an unstressed position.

## Working around an operating railway

None of this happens on a closed site. Access is limited to possession windows,
often at night and measured in hours. That constraint shapes the engineering
rather than just the programme. Details that can be installed quickly, in
sequence, and checked immediately are worth more than details that are marginally
more efficient but need extended access.

## Standards and tools

Analysis and design were carried out to the Eurocodes as adopted in Germany, DIN
EN 1990 through 1998, with DB guideline drawings governing standard details such
as cap widening and parapet adaptation. Finite element modelling used SOFiSTiK,
Dlubal and RFEM. Drawings were produced in Nemetschek and AutoCAD.

The output is a static analysis document suitable for submission and approval,
containing the analysis, cross-sectional drawings, plan overviews and the FEM
model results.
