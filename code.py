import subprocess
def countPoint():
	p = subprocess.run(['timeout', '2s', 'rosrun', 'find_object_2d', 'find_object_2d', 'image:=/camera/rgb/image_raw', '>', 'test.txt'])
	text_file = open("test.txt", "r")
	count = 0
	while(True):
		line = text_file.readline()
		x = line.split()
		breakTime = False
		for i in range (0, len(x)):
			if(x[i]=="descriptors"):
				if(x[i-1]!="Extracting"):
					count= int(x[i-1])
					breakTime = True
					break
		if(breakTime == True):
			break
	return count

test = countPoint()
print(test)
