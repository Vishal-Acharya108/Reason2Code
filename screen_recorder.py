#pip install numpy
#pip install opencv-python
#pip install pyautogui
import numpy as np
import cv2
import pyautogui
screen_width, screen_height = pyautogui.size()
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter(
    r"E:\Reason 2 code\output.avi",
    fourcc,
    20.0,
    (screen_width, screen_height)
)
while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    output.write(frame)
    cv2.imshow("Screen Recorder", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
output.release()
cv2.destroyAllWindows()

