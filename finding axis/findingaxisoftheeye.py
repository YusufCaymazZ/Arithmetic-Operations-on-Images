import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("kara.jpg")

"""cv2.imshow("kara",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Matplotlib graph
plt.imshow(img_rgb, cmap='viridis')
plt.title('Görüntü')
plt.axis('on')
plt.figure(figsize=(16, 16))
plt.show()

#I installed "eye.jpg" from this plot with using vsc, if you using jupyter notebook you will not see the "save as" button.
