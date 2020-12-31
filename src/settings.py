import json

# FUNCTION TO LOAD A PROPERTY FROM A JSON FILE #
def load_from_json(path: str, variable: str) -> list:
	with open(path) as content:
		loaded_json = json.load(content)
		return loaded_json[variable]


# VARIABLES #
MAIL = load_from_json('settings.json', 'mail')
