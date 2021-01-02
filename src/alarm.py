import settings
from playsound import playsound

# FUNCTION TO PLAY ALARM SOUND #
def play_alarm_sound() -> None:
	playsound(settings.ALARMSOUND)
