import cv2 as cv
import time
import HandTrackingModule as htm

# Information about some lines are not given as they are given in the 'HandTrackingModule'

capture = cv.VideoCapture(0)

if not capture.isOpened():
    print("Camera can not be opened!")
    exit()

detectFinger = htm.handDetection()

# Creating an array that stores the IDs of fingertips
tipIDs = [4, 8, 12, 16, 20]

previousTime = 0

# Declaring a variable to count fingers at the end of detection
fingerCount = 0

while True:
    ret, frame = capture.read()
    frame = cv.flip(frame, 1)

    if not ret:
        print("Frames can not be received. Exiting...")
        break

    frame = detectFinger.findHand(frame)
    posList = detectFinger.findPosition(frame, draw=False)
    # The 'draw' parameter is set as 'False' to not to draw second time (due to 'findHand()' function) 

    if len(posList) != 0:

        # Creating an empty array to store situations of fingers
        fingerSituation = []

        # If the Landmark 0 is at the right of the Landmark 1, then there is right hand in the frame
        if posList[0][1] > posList[1][1]:
            rightHand = True
        else:
            rightHand = False

        ########################################
        # If a fingertip's landmark is below the previous two indexes relative to its y-coordinate,
        #   it means that, that finger is closed.
        # But if the thumb is closed, the index of the tip will not be below of the previous index;
        #   it's further to the right if it is right hand.
        # Therefore, the x-coordinate of the thumb tip should be checked, not the y-coordinate.
        ########################################

        # If it is right hand, then the thumb tip will be on the left of the previous index when the finger is up/open
        if rightHand:
            if posList[tipIDs[0]][1] < posList[tipIDs[0]-1][1]:
                # If the finger is opened, then add '1' to the 'fingerSituation' list
                fingerSituation.append(1)
            else:
                # If not, add '0' to the list
                fingerSituation.append(0)
        # If it is left hand, the opposite of the previous check should be performed
        else:
            if posList[tipIDs[0]][1] > posList[tipIDs[0]-1][1]:
                fingerSituation.append(1)
            else:
                fingerSituation.append(0)

        # For the other fingers, the y-coordinate of landmarks should be checked
        for i in range(1, 5):
            if posList[tipIDs[i]][2] < posList[tipIDs[i]-2][2]:
                fingerSituation.append(1)
            else:
                fingerSituation.append(0)

        # Count the '1's in the 'fingerCount' list to determine the number of fingers, which are up
        fingerCount = fingerSituation.count(1)

        # If it is right hand, write 'Right Hand' at the top-right of the frame
        if rightHand:
            cv.putText(frame, "Right Hand", (1010, 95), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        # If it is left hand, write 'Left Hand' at the top-right of the frame
        else:
            cv.putText(frame, "Left Hand", (1025, 95), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        # Write the number of fingers, which are up, at the top-right of the frame
        cv.putText(frame, f"{int(fingerCount)} finger(s) are up", (950, 45), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    currentTime = time.time()
    FPS = 1 / (currentTime - previousTime)
    previousTime = currentTime
    cv.putText(frame, f"FPS: {int(FPS)}", (10, 45), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv.imshow("Finger Counter", frame)

    if cv.waitKey(1) == ord("q"):
        break

capture.release()
cv.destroyAllWindows()