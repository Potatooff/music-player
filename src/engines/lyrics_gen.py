from whisper import load_model
from random import choice; from os import path as pa
from src.utils.paths import gen_lyrics_directory

def gen_lyrics(path: str, save: bool = False, path_to_save: str = gen_lyrics_directory) -> str:
    """ Generate lyrics for a music files with save option"""  
    model = load_model("tiny.en")   # Load whisper smallest model
    result = model.transcribe(path) # transform speech to text

    if save:    # Save lyrics if its on
        rand = "abcderrctvfybghuijimka,lzrthyd45678q4w5tdejyghnbgv"
        path_to_save = pa.join((path_to_save), choice(rand))
        with open(path_to_save, "w") as f:
            f.write(result["text"])
            f.close()
    else:
        pass

    return result["text"]   # Return lyrics
