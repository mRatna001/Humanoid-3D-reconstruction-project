# run.py
# Main pipeline: video → 3D reconstruction → semantic labelling → field notes

import os
import subprocess
import argparse
from semantic import build_person_model, format_field_notes

def extract_frames(video_path, output_folder, fps=2):
    """Extract frames from video using ffmpeg"""
    os.makedirs(output_folder, exist_ok=True)
    cmd = [
        "ffmpeg", "-i", video_path,
        "-vf", f"fps={fps}",
        os.path.join(output_folder, "frame_%04d.png")
    ]
    subprocess.run(cmd, check=True)
    print(f"Frames extracted to {output_folder}")

def run_vggt(image_folder):
    """Run VGGT reconstruction on extracted frames"""
    print("Running VGGT 3D reconstruction...")
    cmd = ["python3", "demo_colmap.py", "--image_folder", image_folder]
    subprocess.run(cmd, check=True)
    print("Reconstruction complete")

def run_semantic(detected_objects):
    """Build person model from detected objects"""
    print("Building person model...")
    model = build_person_model(detected_objects)
    notes = format_field_notes(model)
    return model, notes

def save_outputs(model, notes, output_dir="output"):
    """Save field notes and person model to output folder"""
    os.makedirs(output_dir, exist_ok=True)
    
    with open(os.path.join(output_dir, "field_notes.txt"), "w") as f:
        f.write(notes)
    
    import json
    with open(os.path.join(output_dir, "person_model.json"), "w") as f:
        json.dump(model, f, indent=2)
    
    print(f"Outputs saved to {output_dir}/")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Field Notes: What a robot learns from your room")
    parser.add_argument("--video", type=str, help="Path to input video")
    parser.add_argument("--frames", type=str, default="frames", help="Output folder for frames")
    parser.add_argument("--fps", type=int, default=2, help="Frames per second to extract")
    parser.add_argument("--objects", nargs="+", default=["rug", "lamp", "tapestry", "desk", "books"],
                        help="Objects detected in scene (will be automated with Grounded-SAM)")
    args = parser.parse_args()

    if args.video:
        extract_frames(args.video, args.frames, args.fps)
    
    # semantic inference
    model, notes = run_semantic(args.objects)
    save_outputs(model, notes)
    print("\n" + notes)