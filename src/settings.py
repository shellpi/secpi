import json

# FUNCTION TO LOAD A PROPERTY FROM A JSON FILE #
def load_from_json(path: str, variable: str) -> any:
	with open(path) as content:
		loaded_json = json.load(content)
		return loaded_json[variable]


# VARIABLES #
EMAILSENDERUSR = load_from_json('settings.json', 'email_sender_usr')
EMAILSENDERPSW = load_from_json('settings.json', 'email_sender_psw')
EMAILRECEIVER  = load_from_json('settings.json', 'email_receiver')
EMAILSUBJECT   = load_from_json('settings.json', 'email_subject')
EMAILTEXT      = load_from_json('settings.json', 'email_text')
EMAILSERVERHOST= load_from_json('settings.json', 'SMTP_host')
EMAILSERVERPORT= load_from_json('settings.json', 'SMTP_port')
IMAGEFORMAT    = load_from_json('settings.json', 'image_format')
USEVIDEOPORT   = load_from_json('settings.json', 'use_video_port')
ALARMSOUND     = load_from_json('settings.json', 'alarm_sound')
BUTTONPIN      = load_from_json('settings.json', 'alarm_button_pin')
LEDPIN         = load_from_json('settings.json', 'alarm_led_pin')
