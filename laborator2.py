import numpy as np
import matplotlib.pyplot as plt
from skimage import io
# 1
imgs = np.array([np.load(r"images/car_{idx}.npy".format(idx=i)) for i in range(9)])
#print(imgs)
#
# 2
suma = np.sum(imgs)
print(suma)
#
# 3
sum_c = np.sum(imgs, axis=(1, 2))
#print(sum_c)
#
# 4
print(np.argmax(np.sum(imgs, axis=(1, 2))))
#
# 5
#
# #io.imshow(mean_image.astype(np.uint8))
#
# mean_image = np.mean(imgs, axis=0)
# io.imshow(mean_image.astype(np.uint8))
# io.show()
#
# 6
print(np.std(imgs))
#
# # 1.g
# norm_imgs = (imgs - mean_image) / np.std(imgs)
#
# # 1.h
cropped = imgs[:, 200:301, 290:401]
#
plt.imshow(imgs[7].astype(np.uint), cmap='gray')
#
plt.imshow(cropped[7].astype(np.uint), cmap='gray')