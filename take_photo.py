from PIL import Image
import photos


def get_index(label):
	"""
		read idx.txt file, and get latest image index.
		
		Inputs:
			label - photo label
		
		Outputs:
			idx - index for current photo
	"""
	# initial value of idx is 0
	idx = 0
	
	try:
		with open('photos/idx.txt', 'r', encoding='utf-8') as f:
			idxs = f.readlines()			# read lines
			for i in idxs:
				if(i.split(',')[0] == label):
					idx = int(i.split(',')[1]) + 1
					break
	except:
		print(">>> ERROR: There is a problem opening file {}".format('photos/idx.txt'))
		
	# return idx
	return idx


def update_index(label, idx):
	"""
		update idx.txt
		
		Inputs:
			label - photo label
			idx - index to be update
			
		Outputs:
			None
	"""
	with open('photos/idx.txt', 'r', encoding='utf-8') as f:
		# read lines
		lines = f.readlines()
		# boolean variable to indicate if label is in file
		is_found = 0
		# store result
		lines = [line for line in lines if line is not '\n']
		
		# find label and update
		for i in range(len(lines)):
			if(lines[i].split(',')[0] == label):
				lines[i] = "{},{}\n".format(label, int(idx))
				is_found = 1
			
		# label is not inside the txt file, add into lines
		if(not is_found):
			lines.append("{},{}\n".format(label, 0))
	
	with open('photos/idx.txt', 'w', encoding='utf-8') as f:	
		# write back to the file
		for i in lines:
			f.write(i)



if __name__ == '__main__':
	# default image size
	s = 256
	
	# photo path
	photo_path = 'photos/'
	
	while(True):
		# take a photo
		img = photos.capture_image()
		
		# ask user to enter label
		label = input("Enter photo label: ")
		
		# resize photo according to given size, default is 256x256
		resize_img = img.resize((s, s), Image.ANTIALIAS)
		
		# get last photo index, and add one
		idx = int(get_index(label))
		
		# store photo
		img.save("{}{}_{}.jpg".format(photo_path, label, idx))
		
		# update index
		update_index(label, idx)
