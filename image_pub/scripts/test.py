from jetcam.csi_camera import CSICamera
camera = CSICamera(capture_device=0, width=224, height=224)
frame = camera.read()
