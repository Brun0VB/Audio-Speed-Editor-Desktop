import subprocess
import os

def process_audio(input_file: str, speed: float) -> str:
    if speed < 0.5 or speed > 2.0:
        raise ValueError("Speed must be between 0.5 and 2.0")

    output_file = os.path.splitext(input_file)[0] + f"_speed_{speed}.mp3"

    command = [
        "ffmpeg",
        "-i", input_file,
        "-filter:a", f"atempo={speed}",
        output_file,
        "-y"
    ]

    subprocess.run(command, check=True)

    return output_file