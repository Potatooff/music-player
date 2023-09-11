import whisper


model = whisper.load_model("tiny.en")

result = model.transcribe(r"C:\Users\Hi\Desktop\Songly\test\I_am_wonder.mp3")

with open("lyrics.txt", "w") as f:
    f.write(result["text"])
    f.close()