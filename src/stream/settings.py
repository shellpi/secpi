import json

# FUNCTION TO LOAD A PROPERTY FROM A JSON FILE #
def load_from_json(path: str, variable: str) -> any:
	with open(path) as content:
		loaded_json = json.load(content)
		return loaded_json[variable]


# VARIABLES #
TOKEN = load_from_json('../settings.json', 'streamer_token')
HOST  = load_from_json('../settings.json', 'streamer_host')
PORT  = load_from_json('../settings.json', 'streamer_port')
DEBUG = load_from_json('../settings.json', 'streamer_debug')
