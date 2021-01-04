from mail import send_secpi_email
from camera import get_actual_camera_frame
from detect import detect_if_people
from alarm import alarm
from tools import error

from thread import start_new_thread as snt
from time import sleep

# MAIN FUNCTION #
def main() -> None:
	print ('SecPi 0.1.2 by ShellPi\n')
	while True:
		frame = get_actual_camera_frame()
		if detect_if_people(frame):
			print ('PERSON DETECTED!!')
			try:
				snt( send_secpi_email, (frame, 'Camera view') )
				snt( alarm )
				sleep(10) #Wait 10 seconds
			except Exception as e:
				error(e, 'MultithreadingError')

		else:
			pass
	return None


if __name__ == '__main__':
	main()
