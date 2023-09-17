from moviepy.editor import *
from src.utils.paths import temps_lyrics_directory; from os import path as pa

def Slice_Slay(audio_path: str, segment_duration: int = 28, path_to_save: str = temps_lyrics_directory) -> None:
    
    """Slice audio files"""
    # -----------------------------> segment_durationSlice length
    audio = AudioFileClip(audio_path) # -> File path 
    audio_duration = audio.duration # Audio length 
    num_segments = int(audio_duration / segment_duration)   # Num of parts

    for i in range(num_segments):   # For loops to slice all
        start_time = i * segment_duration
        end_time = (i + 1) * segment_duration
        subclip = audio.subclip(start_time, end_time)
        subclip.write_audiofile(f"segment_{i}.mp3")

    if audio_duration % segment_duration > 0:   # If any part of song left
        start_time = num_segments * segment_duration
        subclip = audio.subclip(start_time, audio_duration)
        path_to_save = pa.join((path_to_save), f"segment_{num_segments}.mp3")
        subclip.write_audiofile(path_to_save)


def Slice_Slay_whisper(audio_path: str, segment_duration: int = 28, path_to_save: str = temps_lyrics_directory):
    
    """Slice audio files"""
    temps_path = []
    # -----------------------------> segment_durationSlice length
    audio = AudioFileClip(audio_path) # -> File path 
    audio_duration = audio.duration # Audio length 
    num_segments = int(audio_duration / segment_duration)   # Num of parts

    for i in range(num_segments):   # For loops to slice all
        start_time = i * segment_duration
        end_time = (i + 1) * segment_duration
        subclip = audio.subclip(start_time, end_time)
        subclip.write_audiofile(f"segment_{i}.mp3")

    if audio_duration % segment_duration > 0:   # If any part of song left
        start_time = num_segments * segment_duration
        subclip = audio.subclip(start_time, audio_duration)
        path_to_save = pa.join(pa.join(path_to_save), f"segment_{num_segments}.mp3")
        temps_path.append(path_to_save)
        subclip.write_audiofile(path_to_save)

    return temps_path
    
