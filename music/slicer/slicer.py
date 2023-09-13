from moviepy.editor import AudioFileClip  # Require moviepy (" pip install moviepy ")

audio = AudioFileClip("bb.mp3") # -> Change for file path 

audio_duration = audio.duration
segment_duration = 28
num_segments = int(audio_duration / segment_duration)

for i in range(num_segments):
    start_time = i * segment_duration
    end_time = (i + 1) * segment_duration
    subclip = audio.subclip(start_time, end_time)
    subclip.write_audiofile(f"segment_{i}.mp3")


if audio_duration % segment_duration > 0:
    start_time = num_segments * segment_duration
    subclip = audio.subclip(start_time, audio_duration)
    subclip.write_audiofile(f"segment_{num_segments}.mp3")

# [ Automatically save files :) ]
