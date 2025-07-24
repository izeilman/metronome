import os, time

def metronome(bpm, duration):
    interval = 60 / bpm
    end_time = time.time() + duration
    print(f"Metronome at {bpm} bpm running for {duration}s...")

    while time.time() < end_time:
        os.system('printf "\a"')  # system beep
        time.sleep(interval)

metronome(100, 120)
