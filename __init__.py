# Ensures MimicMotion/ReActor can import cv2 on headless RunPod workers.
import subprocess
import sys

def _fix():
    try:
        import cv2  # noqa: F401
        return
    except Exception:
        pass
    cmds = [
        [sys.executable, "-m", "pip", "uninstall", "-y", "opencv-python", "opencv-contrib-python"],
        [sys.executable, "-m", "pip", "install", "--no-cache-dir", "opencv-python-headless"],
    ]
    for cmd in cmds:
        try:
            subprocess.run(cmd, check=False)
        except Exception as e:
            print(f"[opencv-headless-fix] {cmd}: {e}")
    try:
        import cv2  # noqa: F401
        print("[opencv-headless-fix] cv2 import ok")
    except Exception as e:
        print(f"[opencv-headless-fix] cv2 still broken: {e}")

_fix()

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}
