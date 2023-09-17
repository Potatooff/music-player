from moviepy.editor import *
from src.utils.paths import temps_lyrics_directory; from os import path as pa
from random import choice
import threading



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
        id = ids()
        temporary = pa.join(pa.join(path_to_save), f"segment_{id}.mp3")
        subclip.write_audiofile(temporary)

    if audio_duration % segment_duration > 0:   # If any part of song left
        start_time = num_segments * segment_duration
        subclip = audio.subclip(start_time, audio_duration)
        id = ids()
        path_to_save = pa.join(pa.join(path_to_save), f"segment_{id}.mp3")
        subclip.write_audiofile(path_to_save)


def Slice_Slay_whisper(audio_path: str, segment_duration: int = 28, path_to_save: str = temps_lyrics_directory):    # ITS WORKING DONT TOUCH IT! ( IT using threading)
    
    """Slice audio files + threaded"""
    # Variables 
    temps_path = []
    audio = AudioFileClip(audio_path) # -> File path 
    audio_duration = audio.duration # Audio length
    num_segments = int(audio_duration / segment_duration)   # Num of parts
    first_thread = int(num_segments / 2)    # Number of segment in first thread
    workload1 = []  # workload of thread1
    workload2 = []  # workload of thread2 

    for w1 in range(first_thread):
        start_time = w1 * segment_duration
        end_time = (w1 + 1) * segment_duration
        timelapse = (start_time, end_time)
        workload1.append(timelapse)
        

    for w2 in range(first_thread, num_segments):
        start_time = w2 * segment_duration
        end_time = (w2 + 1) * segment_duration
        timelapse = (start_time, end_time)
        workload2.append(timelapse)

    def work1():
        for i in workload1:   # For loops to slice all
            start_time, end_time = i
            id = ids()
            temporary = pa.join(pa.join(path_to_save), f"segment_{id}.mp3")
            temps_path.append(temporary)
            subclip = audio.subclip(start_time, end_time)
            subclip.write_audiofile(temporary)

        
    def work2():
        for i in workload2:   # For loops to slice all
            start_time, end_time = i
            subclip = audio.subclip(start_time, end_time)
            id = ids()
            temporary = pa.join(pa.join(path_to_save), f"segment_{id}.mp3")
            temps_path.append(temporary)
            subclip.write_audiofile(temporary)

        if audio_duration % segment_duration > 0:   # If any part of song left
            start_time = num_segments * segment_duration
            subclip = audio.subclip(start_time, audio_duration)
            id = ids()
            final_path = pa.join(pa.join(path_to_save), f"segment_{id}.mp3")
            temps_path.append(final_path)
            subclip.write_audiofile(final_path)

    def run_this_shit():
        thread1 = threading.Thread(target=work1)
        thread1.start()
        thread1.join()
        thread2 = threading.Thread(target=work2)
        thread2.start(); thread2.join()

    run_this_shit()
    return temps_path
