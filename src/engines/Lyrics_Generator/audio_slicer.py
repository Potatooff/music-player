from moviepy.editor import *
from src.utils.paths import temps_lyrics_directory; from os import path as pa
from random import choice


def ids()-> str:
        """ Create a random id for temps files"""
        rand = "abcderrctvfybghuijimkalzrthyd45678q4w5tdejyghnbgv"
        idd = []
        for _ in range(13):
            _ = choice(rand)
            idd.append(_)
        id = "".join(idd)
        return id


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
    
    """ TODO Slice audio files + threaded"""
    # Variables 
    temps_path = []
    audio = AudioFileClip(audio_path) # -> File path 
    audio_duration = audio.duration # Audio length
    num_segments = int(audio_duration / segment_duration)   # Num of parts



    for i in range(num_segments):   # For loops to slice all
        start_time = i * segment_duration    # segment start
        end_time = (i + 1) * segment_duration    # segment end
        subclip = audio.subclip(start_time, end_time)
        id = ids()
        temporary = pa.join(pa.join(path_to_save), f"segment_{id}.mp3")    # Path to save file in temp/lyrics
        temps_path.append(temporary)
        subclip.write_audiofile(temporary)

    if audio_duration % segment_duration > 0:   # save the last segment in temp/lyrics
        start_time = num_segments * segment_duration
        subclip = audio.subclip(start_time, audio_duration)
        id = ids()
        path_to_save = pa.join(pa.join(path_to_save), f"segment_{id}.mp3")
        temps_path.append(path_to_save)
        subclip.write_audiofile(path_to_save)

    return temps_path
    
