import json

# FUNCTION TO LOAD A PROPERTY FROM A JSON FILE #
def load_from_json(path: str, variable: str) -> any:
	with open(path) as content:
		loaded_json = json.load(content)
		return loaded_json[variable]


# TEMPLATE VARIABLES #
index_styles = open('template/index/style.css').read()
index_script = open('template/index/script.js').read()

# CONFIGURATION VARIABLES #
FLIP  = load_from_json('../settings.json', 'flip')
TOKEN = load_from_json('../settings.json', 'streamer_token')
HOST  = load_from_json('../settings.json', 'streamer_host')
PORT  = load_from_json('../settings.json', 'streamer_port')
DEBUG = load_from_json('../settings.json', 'streamer_debug')
