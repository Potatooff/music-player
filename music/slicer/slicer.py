from moviepy.editor import AudioFileClip


def Slice_Slay(path, segment_duration: int = 28) -> None:
    """Slice audio files"""
    # -----------------------------> segment_durationSlice length
    audio = AudioFileClip(path) # -> File path 
    audio_duration = audio.duration # Audio length 
    num_segments = int(audio_duration / segment_duration)   # Num of parts

    for i in range(num_segments):
        start_time = i * segment_duration
        end_time = (i + 1) * segment_duration
        subclip = audio.subclip(start_time, end_time)
        subclip.write_audiofile(f"segment_{i}.mp3")

    if audio_duration % segment_duration > 0:   # If any part of song left
        start_time = num_segments * segment_duration
        subclip = audio.subclip(start_time, audio_duration)
        subclip.write_audiofile(f"segment_{num_segments}.mp3")
# Automatically saves files! in the same directory need to change that
