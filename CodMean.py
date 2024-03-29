import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets.samples_generator import make_blobs
from itertools import cycle
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
#%matplotlib inline
pylab.rcParams['figure.figsize'] = 16, 12
image = Image.open('GITS_ANIME.jpg')

# Transformar em matriz
image = np.array(image)

#Reshape
original_shape = image.shape
X = np.reshape(image, [-1, 3])

#Plotar imagem e estimar a banda
plt.imshow(image)

bandwidth = estimate_bandwidth(X, quantile=0.1, n_samples=100)
print(bandwidth)

#Trabalhar com a banda estimada uma vez só, muito lento
ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(X)
labels = ms.labels_
print(labels.shape)
cluster_centers = ms.cluster_centers_
print(cluster_centers.shape)

labels_unique = np.unique(labels)
n_clusters_ = len(labels_unique)

print("Número de clusters estimados : %d" % n_clusters_)
segmented_image = np.reshape(labels, original_shape[:2])  # Just take size, ignore RGB channels.
plt.figure(2)
plt.subplot(1, 2, 1)
plt.imshow(image)
#plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(segmented_image)
plt.axis('off')
print("FIM")
