# my_functions.py
from __future__ import print_function, unicode_literals
from facepplib import FacePP, exceptions


def calculate_result():
    # Perform your calculations and return the result
    result = 42  # Replace with your actual calculation
    return result


# define global variables
face_detection = ""
faceset_initialize = ""
face_search = ""
face_landmarks = ""
dense_facial_landmarks = ""
face_attributes = ""
beauty_score_and_emotion_recognition = ""

# define face comparing function
def face_comparing(app, Image1, Image2): 
	
	print()
	print('-'*30)
	print('Comparing Photographs......')
	print('-'*30)


	cmp_ = app.compare.get(image_url1 = Image1,
						image_url2 = Image2)

	print('Photo1', '=', cmp_.image1)
	print('Photo2', '=', cmp_.image2)

	# Comparing Photos
	if cmp_.confidence > 70:
		# print('Both photographs are of same person......')
		return 1
	else:
		# print('Both photographs are of two different persons......')
		return 0

		
# Driver Code

def main(image1, image2)->int:
    api_key ='xQLsTmMyqp1L2MIt7M3l0h-cQiy0Dwhl'
    api_secret ='TyBSGw8NBEP9Tbhv_JbQM18mIlorY6-D'

		# call api
    app_ = FacePP(api_key = api_key,
					api_secret = api_secret)
	
		# face_comparing(app_, image1, image2)		
    output = face_comparing(app_, image1, image2)
    if(output == 1):
        return 1
    return 0

# image1 = val
image2 = 'https://i.postimg.cc/HLrk9ZND/Photo-on-09-05-23-at-19-51.jpg'	
# a = main(image1, image2)
