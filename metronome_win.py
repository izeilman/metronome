import winsound, time

def metronome(bpm, duration, freq=1200, ms=50):
    interval = 60 / bpm
    end_time = time.time() + duration
    print(f"Metronome at {bpm} BPM for {duration} seconds.")
    
    while time.time() < end_time:
        winsound.Beep(freq, duration_ms)
        time.sleep(max(0, interval - (duration_ms/1000)))

metronome(100, 120, freq=1200, duration=30)
