import settings
import tools
from playsound import playsound
from gpiozero import LED, Button

from time import sleep
import thread


# FUNCTION TO PLAY ALARM SOUND #
def play_alarm_sound(button: Button) -> None:
	while !button.is_pressed:
		playsound(settings.ALARMSOUND)


# FUNCTION TO TURN THE ALARM LED ON #
def alarm_led_ON(led: LED, button: Button) -> None:
	while !button.is_pressed:
		led.on()
		sleep(1)
		led.off
		sleep(1)


# PLAY THE ALARM WHILE BUTTON IS NOT PRESSED #
def alarm() -> None:
	button = Button(settings.BUTTONPIN)
	led    = LED(settings.LEDPIN)

	try:
		thread.start_new_thread( play_alarm_sound, (button) )
		thread.start_new_thread( alarm_led_ON, (led, button) )
	except Exception as e:
		tools.error(e, 'MultithreadingError')
