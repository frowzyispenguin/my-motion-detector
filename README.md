# My Motion Detector

it's an script which watches your webcam source as a CCTV and write logs of motion inside the room in a text file 

# Changing Video Source
**[1] WebCam**

for using your secondary webcam 
change this part of code : 
`cap = cv2.VideoCapture(0) `

note : 0 is your main web cam then other ones is 1 , 2, 3 and ..

EXAMPLE : my secondary webcam (second one in this example ) is available 
I would change `cap = cv2.VideoCapture(0) `
to `cap = cv2.VideoCapture(1) `

**[2] OfflineSource**

for parsing offline data you can change above example source 
use video name(wich is in the same directory of script) instead of webcam source

EXAMPLE : my video name is "video.mp4"
I would change `cap = cv2.VideoCapture(0) `
to `cap = cv2.VideoCapture("video.mp4") `



