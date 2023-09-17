from whisper import load_model
from random import choice; from os import path as pa
from src.utils.paths import temps_lyrics_directory
from src.ui.error.error_page import error_window
from src.engines.Lyrics_Generator.audio_slicer import Slice_Slay_whisper as slice_audio
import threading

threads = []

num_runs = 2

# TODO ADD GPU USAGE INSTEAD OF CPU FOR WHISPER MODEL BECUZ YES IT IS USING ONLY CPU I THINK

def gen_lyrics(path: str, save: bool = True, path_to_save: str = temps_lyrics_directory) -> str:
    """ Generate lyrics for a music files with save option"""  

    def ids()-> str:
        """ Create a random id for temps files"""
        rand = "abcderrctvfybghuijimkalzrthyd45678q4w5tdejyghnbgv"
        idd = []
        for _ in range(13):
            _ = choice(rand)
            idd.append(_)
        idd.append(".txt")
        id = "".join(idd)
        return id

    work = slice_audio(path)   
    model = load_model("tiny.en")   # Load whisper smallest model

    for _ in work:
        lyrics = ""
        result = model.transcribe(_, temperature=0.2, fp16=False) # transform speech to text
        result_formatted = result["text"]
        lyrics = f"{lyrics}\n{result_formatted}"
        if save:    # Save lyrics if it on True
            try:
                id = ids()
                path_to_save = pa.join(pa.join(path_to_save), choice(id))
                with open(path_to_save, "wt") as f:
                    f.write(lyrics)
                    
            except Exception as e:
                error_window(e)

            finally:
                f.close()

    return lyrics  # Return generated lyrics
