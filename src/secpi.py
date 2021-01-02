from mail import send_secpi_email
from camera import get_actual_camera_frame
from detect import detect_if_people

from time import sleep

# MAIN FUNCTION #
def main() -> None:
	while True:
		frame = get_actual_camera_frame()
		if detect_if_people(frame):
			send_secpi_email(frame, 'Camera view')
			sleep(10000) #Wait 10 seconds
		else:
			pass
	return None
