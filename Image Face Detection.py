import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Read the frame
img = cv2.imread('IMG.jpg')

    # Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
faces = face_cascade.detectMultiScale(gray, 1.4, 4)

    # Draw the rectangle around each face
for (x, y, w, h) in faces:
    cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display
cv2.imshow('Image', gray)
cv2.waitKey()
