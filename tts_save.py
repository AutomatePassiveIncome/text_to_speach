from pyfreetts import Text2Speech
import os

module = Text2Speech()
module.setup_voice("am")
with open('text.txt', 'r') as file:
    text = file.read()
module.convert(text)
i = 0
while os.path.exists(f"file_{i}.mp3"):
    i += 1
module.save_to_file(f"file_{i}.mp3")

module.close()