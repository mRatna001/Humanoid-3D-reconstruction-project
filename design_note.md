# Design Note

## What I built

A system that takes a short phone video of a room, reconstructs it in 3D, and generates a structured operational profile of the person who lives there — built entirely from physical evidence.

The output isn't a personality profile. It's a behavioural map: what a humanoid robot would need to know to operate safely and appropriately alongside the person who inhabits that space.

## Why this framing

Most 3D reconstruction pipelines stop at geometry. This one treats geometry as a starting point. A robot that can navigate a room is useful. A robot that understands the room — what matters in it, where to be careful, what the space says about its occupant — is more useful.

The test case is my own room: Persian rugs, hand-sewn tapestries, a rocket-shaped lava lamp, objects accumulated over years. The field notes it generates could only come from this room. That specificity is the point.

## Technical choices

**VGGT over COLMAP + 3DGS**
COLMAP solves geometry iteratively from matched keypoints. VGGT is a feed-forward transformer that predicts depth maps, camera parameters, and point clouds in a single pass — no iterative optimisation. It's faster, more robust on textureless surfaces, and represents the direction the field is moving. It won Best Paper at CVPR 2025.

**Rule-based inference over a VLM**
I chose to write the semantic inference rules myself rather than delegating to a vision-language model. This makes every inference traceable — you can see exactly why the system concluded what it did. A VLM would produce richer output but the reasoning would be opaque. For a robot operating in someone's home, transparency matters.

**Field notes format**
The output is structured like operational field notes rather than a narrative description. Dry, specific, observational. The framing is: this is what a robot records after entering an unknown space for the first time.

## Tradeoffs

- Grounded-SAM integration for automatic object detection is partially implemented. Currently the object list can be passed manually or detected via the semantic pipeline.
- Reconstruction quality scales with number of input frames and GPU memory. Tested on RTX 4070 (8GB) with 28-50 frames and on A100 (80GB) with 227 frames.
- The rule set is hand-crafted for this room. A production system would learn rules from data.

## What I'd do with more time

- Full Grounded-SAM integration to automatically detect and label objects in the 3D point cloud
- Interactive 3D viewer where clicking an object shows its contribution to the person model
- Gaussian Splatting renders for higher visual quality
- Expand the rule set and validate against multiple rooms