import numpy as np
import cv2
import scipy.linalg as s_linalg


class pca_class:
    def __init__(self, images, y, target_names, no_of_elements, quality_percent):
        self.no_of_elements = no_of_elements
        self.images = np.asarray(images)
        self.y = y
        self.target_names = target_names
        mean = np.mean(self.images, 1)
        self.mean_face = np.asmatrix(mean).T
        self.images = self.images - self.mean_face
        self.quality_percent = quality_percent

    def give_p(self,d): # Singular value and variace and Quality Percent
        sum = np.sum(d)
        sum_85 = self.quality_percent * sum/100
        temp = 0
        p = 0
        while temp < sum_85:
            temp += d[p]
            p += 1
        # print("value of p and d : " ,p ,d)
        return p

    def reduce_dim(self):

        u, sigma,vt= s_linalg.svd(self.images, full_matrices=True)
        u_matrix = np.matrix(u)
        sigma_diag = np.diag(sigma)
        vt_matrix = np.matrix(vt)
        u = self.give_p(sigma)
        self.new_bases = u_matrix[:, 0:u]
        print("new bases",self.new_bases.shape)
        self.new_coordinates = np.dot(self.new_bases.T, self.images)
        return self.new_coordinates.T
    
    def original_data(self, new_coordinates):
        return self.mean_face + (np.dot(self.new_bases, new_coordinates.T))





   