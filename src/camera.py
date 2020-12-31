import settings
import tools
import picamera

# FUNCTION TO GET THE ACTUAL CAMERA FRAME #
def get_actual_camera_frame() -> file:
	camera_output = open('.secpi.camera.tmp')
	with picamera.PiCamera() as camera:
		try:
			camera.capture(camera_output, 
			               settings.IMAGEFORMAT,
				       use_video_port=settings.USEVIDEOPORT)
		except Exception as e:
			tools.error(e, 'CameraError')
