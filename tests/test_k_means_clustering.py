from parameterized import parameterized
import unittest.mock as mock
import unittest
import sys
import os
import numpy as np
import random

#import capture_output
sys.path.append(os.path.abspath('../machine_learning'))
import k_means_clust

class KMeansTestCase(unittest.TestCase):

	test_data = [
		[[-5, -4, -7, -2, -7], [5, -10, 8, 8, -3], [0, -4, 6, -2, 6], [-1, -1, 5, 9, 5], [-6, 3, -10, -5, -5]],
		[[9, -9, -7, 3, -9], [-5, -2, 0, -6, -10], [4, 1, 2, -10, 8], [-8, 8, 2, -5, -3], [7, -1, -6, 6, -8]],
		[[0, 7, -5, 4, 3], [2, 1, -8, 8, 4], [7, -6, -1, -7, 5], [2, -7, -10, -3, -1], [-1, -3, -3, -6, 9]],
		[[-2, 7, -9, 8, -5], [-8, -5, 9, 1, 6], [-8, -3, -8, 0, 4], [-4, -6, -6, 6, 1], [-5, 2, -2, -9, 9]],
		[[2, -4, 2, -1, 7], [-6, -6, -10, 3, -5], [-7, 4, 9, -6, -5], [-9, 3, -3, -6, -10], [-1, -5, -5, -4, -3]]
	]
	
	test_centroids = [
		[[-1, -1, 5, 9, 5], [-6, 3, -10, -5, -5], [-5, -4, -7, -2, -7], [5, -10, 8, 8, -3]],
		[[-8, 8, 2, -5, -3], [7, -1, -6, 6, -8], [9, -9, -7, 3, -9], [-5, -2, 0, -6, -10],
		 [-8, 8, 2, -5, -3], [9, -9, -7, 3, -9], [9, -9, -7, 3, -9], [-5, -2, 0, -6, -10], 
		 [7, -1, -6, 6, -8]],
		[[2, -7, -10, -3, -1], [-1, -3, -3, -6, 9]],
		[[-4, -6, -6, 6, 1], [-5, 2, -2, -9, 9], [-2, 7, -9, 8, -5], [-8, -5, 9, 1, 6], [-4, -6, -6, 6, 1], 
		 [-2, 7, -9, 8, -5], [-2, 7, -9, 8, -5], [-8, -5, 9, 1, 6]],
		[[-9, 3, -3, -6, -10], [-1, -5, -5, -4, -3], [2, -4, 2, -1, 7]]
	]
	
	test_distances = [
		[[20.83266666, 8.48528137, 0, 21.84032967], [13.82027496, 28.05352028, 21.84032967, 0],
       	 [11.53256259, 21.70253441, 19.05255888, 15.68438714], [0, 23.70653918, 20.83266666, 13.82027496],
       	 [23.70653918, 0, 8.48528137, 28.05352028]],
       	[[27.54995463, 8.88819442, 0, 19.39071943, 27.54995463, 0, 0, 19.39071943, 8.88819442],
       	 [12.76714533, 18.13835715, 19.39071943, 0, 12.76714533, 19.39071943, 19.39071943, 0, 18.13835715],
       	 [18.41195264, 24.2693222 , 25.76819745, 20.83266666, 18.41195264, 25.76819745, 25.76819745, 20.83266666, 24.2693222],
       	 [0, 22.71563338, 27.54995463, 12.76714533, 0, 27.54995463, 27.54995463, 12.76714533, 22.71563338],
         [22.71563338, 0, 8.88819442, 18.13835715, 22.71563338, 8.88819442, 8.88819442, 18.13835715, 0]],
        [[17.02938637, 15.5241747], [14.62873884, 16.46207763], [12.60952021, 9.69535971],
         [0, 13.52774926], [13.52774926, 0]],
        [[14.89966443, 23.83275058, 0, 25.96150997, 14.89966443, 0, 0, 25.96150997],
         [17.08800749, 16.97056275, 25.96150997, 0, 17.08800749, 25.96150997, 25.96150997, 0],
         [8.60232527, 13.26649916, 16.79285562, 17.2626765 , 8.60232527, 16.79285562, 16.79285562, 17.2626765],
         [0, 19.23538406, 14.89966443, 17.08800749, 0, 14.89966443, 14.89966443, 17.08800749],
         [19.23538406, 0, 23.83275058, 16.97056275, 19.23538406, 23.83275058, 23.83275058, 16.97056275]],
        [[22.56102835, 12.9614814 , 0], [15.65247584, 10.19803903, 19.28730152], [13.19090596, 17.91647287, 19.05255888],
         [0, 13.60147051, 22.56102835], [13.60147051, 0, 12.9614814]]
    ]
   
	test_assignments = [
		[2, 3, 0, 0, 1], [2, 3, 0, 0, 1], [1, 0, 1, 0, 1], [2, 3, 0, 0, 1], [2, 1, 0, 0, 1]
    ]
   		

	@parameterized.expand([
		("test_1", test_data[0], 4, test_centroids[0]),
		("test_2", test_data[1], 9, test_centroids[1]),
		("test_3", test_data[2], 2, test_centroids[2]),
		("test_4", test_data[3], 8, test_centroids[3]),
		("test_5", test_data[4], 3, test_centroids[4])])
	def test_get_initial_centroids(self, _, data, k, expected):
		array = np.array(data)
		np.testing.assert_equal(k_means_clust.get_initial_centroids(array, k, seed=1).tolist(), expected)

	@parameterized.expand([
		("test_1", test_data[0], test_centroids[0], test_distances[0]),
		("test_2", test_data[1], test_centroids[1], test_distances[1]),
		("test_3", test_data[2], test_centroids[2], test_distances[2]),
		("test_4", test_data[3], test_centroids[3], test_distances[3]),
		("test_5", test_data[4], test_centroids[4], test_distances[4])])
	def test_centroid_pairwise_dist(self, _, data, data2, expected):
		X = np.array(data)
		centroids = np.array(data2)
		np.testing.assert_almost_equal(k_means_clust.centroid_pairwise_dist(X, centroids).tolist(), expected, decimal=6)
		
	@parameterized.expand([
		("test_1", test_data[0], test_centroids[0], test_assignments[0]),
		("test_2", test_data[1], test_centroids[1], test_assignments[1]),
		("test_3", test_data[2], test_centroids[2], test_assignments[2]),
		("test_4", test_data[3], test_centroids[3], test_assignments[3]),
		("test_5", test_data[4], test_centroids[4], test_assignments[4])])
	def test_assign_clusters(self, _, data, data2, expected):
		test_data = np.array(data)
		centroids = np.array(data2)
		np.testing.assert_equal(k_means_clust.assign_clusters(test_data, centroids), expected)
	

if __name__ == "__main__":   
	unittest.main()