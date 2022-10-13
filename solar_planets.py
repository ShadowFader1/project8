import cv2
from cv2 import putText
img = cv2.imread("solar-system.jpg")
cv2.putText(img,
"Sun",
(20,300),
cv2.FONT_HERSHEY_COMPLEX,
.5,
(255,255,255)
)

cv2.putText(img,
"Mercury",
(100,300),
cv2.FONT_HERSHEY_COMPLEX,
.5,
(255,255,255)
)

cv2.putText(img,
"Venus",
(200,300),
cv2.FONT_HERSHEY_COMPLEX,
.5,
(255,255,255)
)

cv2.putText(img,
"Earth",
(300,300),
cv2.FONT_HERSHEY_COMPLEX,
.5,
(255,255,255)
)

cv2.putText(img,
"Mars",
(400,300),
cv2.FONT_HERSHEY_COMPLEX,
.5,
(255,255,255)
)

cv2.putText(img,
"Jupiter",
(500,300),
cv2.FONT_HERSHEY_COMPLEX,
.5,
(255,255,255)
)

cv2.putText(img,
"Saturn",
(800,300),
cv2.FONT_HERSHEY_COMPLEX,
.5,
(255,255,255)
)

cv2.putText(img,
"Uranus",
(1000,300),
cv2.FONT_HERSHEY_COMPLEX,
.5,
(255,255,255)
)

cv2.putText(img,
"Neptune",
(1100,300),
cv2.FONT_HERSHEY_COMPLEX,
.5,
(255,255,255)
)

cv2.imshow("output",img)
cv2.waitKey(0)
