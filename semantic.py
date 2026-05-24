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

def build_person_model(detected_objects):
    """
    Takes a list of detected object labels and builds a structured
    person model based on rules.
    
    detected_objects: list of strings e.g. ["rug", "desk", "lamp"]
    returns: dict representing what a robot has inferred about the occupant
    """
    
    person_model = {
        "objects_detected": detected_objects,
        "zones": [],
        "robot_behaviours": [],
        "high_significance_objects": [],
        "activity_profile": [],
        "confidence": "medium"
    }
    
    for obj in detected_objects:
        if obj in OBJECT_RULES:
            rule = OBJECT_RULES[obj]
            
            person_model["zones"].append(rule["zone_type"])
            person_model["robot_behaviours"].append(rule["robot_behaviour"])
            
            if rule["significance"] in ["high", "very_high"]:
                person_model["high_significance_objects"].append(obj)
            
            if rule["activity"] not in person_model["activity_profile"]:
                person_model["activity_profile"].append(rule["activity"])
    
    # remove duplicates
    person_model["zones"] = list(set(person_model["zones"]))
    person_model["robot_behaviours"] = list(set(person_model["robot_behaviours"]))
    
    return person_model

def format_field_notes(person_model, date=None):
    """
    Formats the person model as field notes — structured, observational,
    scientific. Not a story. Evidence.
    """
    from datetime import datetime
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    
    lines = [
        "FIELD NOTES",
        f"Date: {date}",
        f"Observer: HMND-01",
        "",
        "OBJECTS IDENTIFIED",
    ]
    
    for obj in person_model["objects_detected"]:
        if obj in OBJECT_RULES:
            lines.append(f"  - {obj}: {OBJECT_RULES[obj]['notes']}")
    
    lines += [
        "",
        "ZONE ANALYSIS",
        f"  Active zones: {', '.join(person_model['zones'])}",
        f"  Activity profile: {', '.join(person_model['activity_profile'])}",
        "",
        "HIGH SIGNIFICANCE OBJECTS",
        f"  {', '.join(person_model['high_significance_objects']) if person_model['high_significance_objects'] else 'none identified'}",
        "",
        "ROBOT BEHAVIOUR DIRECTIVES",
    ]
    
    for behaviour in person_model["robot_behaviours"]:
        lines.append(f"  - {behaviour}")
    
    lines += [
        "",
        f"Confidence: {person_model['confidence']}",
        "Note: Model derived from single-room observation."
    ]
    
    return "\n".join(lines)


if __name__ == "__main__":
    # test with example objects from Maira's room
    test_objects = ["rug", "lamp", "tapestry", "desk", "books"]
    model = build_person_model(test_objects)
    print(format_field_notes(model))