import json
from stream import start_stream
from input import InputClient

config = json.load(open("config.json"))

print("🎮 DogNTR starting...")

input_client = InputClient(
    config["3ds_ip"],
    config["input_port"]
)

start_stream(config["video_port"])
