import json

# FUNCTION TO LOAD A PROPERTY FROM A JSON FILE #
def load_from_json(path: str, variable: str) -> any:
	with open(path) as content:
		loaded_json = json.load(content)
		return loaded_json[variable]


# TEMPLATE VARIABLES #
index_styles = open('template/index/style.css').read()
index_script = open('template/index/script.js').read()

# CAMERA VARIABLES #
NAME  = load_from_json('../settings.json', 'name')
OWNER = load_from_json('../settings.json', 'owner')

# CONFIGURATION VARIABLES #
FLIP  = load_from_json('../settings.json', 'flip')
HOST  = load_from_json('../settings.json', 'streamer_host')
PORT  = load_from_json('../settings.json', 'streamer_port')
DEBUG = load_from_json('../settings.json', 'streamer_debug')
USERS = load_from_json('../settings.json', 'users')
