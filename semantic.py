# semantic.py
# Rule-based person model inference from detected objects in 3D space

OBJECT_RULES = {
    "rug": {
        "zone_type": "soft_floor",
        "activity": "relaxation_social",
        "robot_behaviour": "careful_movement",
        "significance": "high",
        "notes": "Textile floor covering — avoid dragging objects across"
    },
    "desk": {
        "zone_type": "work",
        "activity": "focused_work",
        "robot_behaviour": "avoid_interruption",
        "significance": "high",
        "notes": "High-value objects likely present — handle with care"
    },
    "lamp": {
        "zone_type": "lighting",
        "activity": "frequent_access",
        "robot_behaviour": "maintain_clearance",
        "significance": "medium",
        "notes": "Frequently accessed by occupant — potential heat hazard"
    },
    "tapestry": {
        "zone_type": "wall_mounted",
        "activity": "display",
        "robot_behaviour": "do_not_touch",
        "significance": "very_high",
        "notes": "Handmade — high sentimental value, fragile"
    },
    "books": {
        "zone_type": "storage",
        "activity": "reading_reference",
        "robot_behaviour": "careful_handling",
        "significance": "high",
        "notes": "Indicates sustained intellectual interest — do not reorder"
    },
    "plant": {
        "zone_type": "living",
        "activity": "care_required",
        "robot_behaviour": "avoid_blocking_light",
        "significance": "medium",
        "notes": "Living object — do not move, needs light access"
    },
    "sports_equipment": {
        "zone_type": "active",
        "activity": "physical_exercise",
        "robot_behaviour": "clear_pathways",
        "significance": "medium",
        "notes": "Indicates active lifestyle — keep movement zones clear"
    }
}
