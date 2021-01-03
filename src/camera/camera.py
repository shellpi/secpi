import settings
import tools
import picamera

# FUNCTION TO GET THE ACTUAL CAMERA FRAME #
def get_actual_camera_frame() -> any:
	camera_output = open('/tmp/.secpi.camera.tmp', 'wb+')
	with picamera.PiCamera() as camera:
		try:
			camera.capture(camera_output, 
			               settings.IMAGEFORMAT,
				       use_video_port=settings.USEVIDEOPORT)
			return camera_output.read()
		except Exception as e:
			tools.error(e, 'CameraError')
