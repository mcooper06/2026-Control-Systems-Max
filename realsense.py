import pyrealsense2 as rs
import numpy as np

# control is the pipeline which acts as a start/stop
control = rs.pipeline()

# config enables the confgiuration of non-default streams through config.enable_stream(...)
config = rs.config()

distance_arr = np.array([])


######  START  ######

config.enable_device_from_file("d435i_walking.bag")
control.start(config)

# add buffer time for auto-exposure
for i in range(5):
    control.wait_for_frames()

first_frame = control.wait_for_frames()
first_depth = first_frame.get_depth_frame()
width = first_depth.get_width()                 # 1280
height = first_depth.get_height()               # 720     

for w in range(100):
    for h in range(100):
        frames = control.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        distance = depth_frame.get_distance(w, h)
        print("Distance at pixel ({}, {}): {} meters".format(w, h, distance))
        if not depth_frame:     
            pass
    


control.stop()

######  STOP  ######
