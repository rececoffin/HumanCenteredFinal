import subprocess
p = subprocess.Popen("roscore", stdout=subprocess.PIPE, shell=True)
#change to camera that is used 
p = subprocess.Popen("rosrun uvc_camera uvc_camera_node &", stdout=subprocess.PIPE, shell=True)
p = subprocess.Popen("rosrun find_object_2d find_object_2d image:=image_raw", stdout=subprocess.PIPE, shell=True)
p = subprocess.Popen("rosrun find_object_2d print_objects_detected", stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
file_object  = open("file.txt","w")
file_object.write(output)
#might have to translates positions to take start into account
