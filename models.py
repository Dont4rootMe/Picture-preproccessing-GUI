from sklearn.cluster import estimate_bandwidth
import numpy as np
from cv2 import connectedComponentsWithStats


def count_bounded_parts(grayscale_img) -> tuple[int, tuple[np.array, np.array]]:
    img_map = np.array(grayscale_img)
    num_labels, labels, stats, centroids = \
        connectedComponentsWithStats(img_map, 8)

    return num_labels - 1, (np.ravel(centroids[:, 1].astype(int)), np.ravel(centroids[:, 0].astype(int)))
