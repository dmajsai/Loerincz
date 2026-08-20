---
title: "Concrete frame rail bridge on a special anchor foundation"
description: >-
  Design and analysis of a reinforced concrete frame rail bridge founded on
  bored piles with a special anchor arrangement, where ground conditions and
  groundwater governed the foundation concept.
date: 2026-08-18
cluster: railway-bridges
cluster_name: Railway bridges
client: DB German Rail
scope: Design and planning
structure: Reinforced concrete frame, piled foundation
services: Structural design, structural analysis, geotechnical checks
image: /images/unnamed-27.png
image_alt: >-
  Geotechnical cross-section showing a concrete frame structure founded on bored
  piles, with soil layer properties and groundwater level marked
image_caption: >-
  Cross-section through the frame and its piled foundation, with soil layers,
  unit weights, friction angles and groundwater level.
---

When a frame structure sits in weak ground with high groundwater, the foundation
stops being a detail that follows the superstructure design and becomes the thing
that determines it.

This project covered design and analysis of a concrete frame structure with a
special anchor foundation for a railway bridge in the DB German Rail network.

## Reading the ground first

The section through this structure records what the analysis had to work with:
distinct soil layers each with their own unit weight and friction angle, a
groundwater level sitting above founding level, and a bored pile solution taken
down past the weaker material.

Those numbers set the problem. Layers with low friction angles will not carry the
frame on spread footings at a sensible depth, so load has to be taken to
competent material below. Groundwater above founding level introduces uplift on
the structure and requires the excavation to be supported and dewatered rather
than simply cut.

## Why an anchor arrangement is needed

A buried frame in high groundwater has a problem that surface structures do not.
The structure displaces water, and the water pushes back. When the buoyant force
exceeds the weight of the structure and the material above it, the frame wants to
float.

There are three ways to deal with it. Add enough weight to hold the structure
down, which is expensive and adds load to ground that was weak to begin with.
Rely on friction from surrounding material, which is unreliable and cannot be
counted on in saturated ground. Or anchor the structure into competent material
below, which is what a special anchor foundation does.

Anchored piles work in tension rather than compression, which reverses the usual
design assumption. The pile has to develop uplift resistance through shaft
friction along its embedded length, the connection between pile and base slab has
to transfer tension rather than bearing, and the reinforcement has to be
continuous through a joint that would otherwise just be a construction detail.

The governing case is often not the finished structure in service. It is the
structure complete but not yet backfilled, when the weight holding it down is at
its lowest and the water table has recovered after dewatering stops. That
temporary condition has to be checked explicitly, and it frequently controls the
anchor design.

## Frame and foundation as one system

A frame founded on piles cannot be analysed as a frame sitting on fixed supports.
Pile stiffness affects how moment distributes through the frame, and differential
settlement between piles introduces forces that a rigid-support model never
produces.

The practical approach is to model the piles as springs with stiffness derived
from the geotechnical assessment, then check the frame against a range of
stiffness values rather than a single figure. Ground stiffness is never known
precisely, and a design that only works for one assumed value is not a design.

Earth pressure on the frame walls is part of the same system. Active and at-rest
pressure give different answers, and which applies depends on whether the wall can
move enough to mobilise active conditions. For a stiff closed frame it usually
cannot, so at-rest pressure governs and the walls carry more than a retaining wall
of the same height would.

## Standards and tools

Design followed the Eurocodes as adopted in Germany, DIN EN 1990 through 1998,
with DIN EN 1997 governing the geotechnical design of the piles and the
verification against uplift. Structural analysis used SOFiSTiK, Dlubal and RFEM.
Geotechnical checks, including pile capacity and earth pressure, were carried out
in GGU.

The static analysis document covers the frame model, the pile design in both
compression and tension, the uplift verification for the temporary and permanent
cases, and the reinforcement drawings for the pile-to-slab connection.
