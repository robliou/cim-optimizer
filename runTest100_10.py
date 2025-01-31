#Initialization and Imports
import sys
import numpy as np

from pathlib import Path
sys.path.append(str(Path.cwd()) + "\\..\\") # append repo to list of search directories

from cim_optimizer.solve_Ising import *
from cim_optimizer.CIM_helper import brute_force
import time
start_time = time.perf_counter()

lst =  [[0, 12, 1], [0, 15, 1], [0, 53, 1], [0, 90, 1], [1, 27, 1], [1, 42, 1], [1, 65, 1], [1, 69, 1], [1, 76, 1], [1, 82, 1], [1, 83, 1], [1, 85, 1], [1, 97, 1], [2, 12, 1], [2, 37, 1], [2, 39, 1], [2, 60, 1], [2, 67, 1], [2, 72, 1], [2, 82, 1], [2, 86, 1], [2, 87, 1], [2, 88, 1], [2, 98, 1], [3, 17, 1], [3, 24, 1], [3, 31, 1], [3, 46, 1], [3, 55, 1], [3, 62, 1], [3, 77, 1], [3, 79, 1], [3, 82, 1], [3, 83, 1], [3, 86, 1], [3, 92, 1], [3, 94, 1], [3, 98, 1], [4, 6, 1], [4, 9, 1], [4, 11, 1], [4, 26, 1], [4, 27, 1], [4, 28, 1], [4, 33, 1], [4, 39, 1], [4, 41, 1], [4, 48, 1], [4, 51, 1], [4, 60, 1], [4, 65, 1], [4, 72, 1], [4, 81, 1], [4, 82, 1], [4, 87, 1], [5, 43, 1], [5, 47, 1], [5, 48, 1], [5, 51, 1], [5, 60, 1], [5, 61, 1], [5, 81, 1], [5, 86, 1], [5, 89, 1], [5, 99, 1], [6, 4, 1], [6, 15, 1], [6, 23, 1], [6, 36, 1], [6, 42, 1], [6, 60, 1], [6, 61, 1], [6, 66, 1], [6, 72, 1], [6, 77, 1], [6, 78, 1], [6, 85, 1], [6, 92, 1], [7, 24, 1], [7, 74, 1], [7, 85, 1], [7, 94, 1], [8, 19, 1], [8, 47, 1], [8, 62, 1], [8, 66, 1], [8, 70, 1], [8, 72, 1], [8, 75, 1], [8, 92, 1], [8, 94, 1], [8, 97, 1], [9, 4, 1], [9, 10, 1], [9, 14, 1], [9, 29, 1], [9, 42, 1], [9, 47, 1], [9, 49, 1], [9, 52, 1], [9, 64, 1], [9, 68, 1], [9, 85, 1], [9, 92, 1], [9, 94, 1], [10, 9, 1], [10, 22, 1], [10, 26, 1], [10, 28, 1], [10, 34, 1], [10, 45, 1], [10, 61, 1], [10, 76, 1], [10, 85, 1], [10, 86, 1], [10, 96, 1], [11, 4, 1], [11, 14, 1], [11, 17, 1], [11, 21, 1], [11, 26, 1], [11, 40, 1], [11, 58, 1], [11, 63, 1], [11, 69, 1], [11, 70, 1], [11, 74, 1], [11, 78, 1], [11, 87, 1], [11, 96, 1], [12, 0, 1], [12, 2, 1], [12, 34, 1], [12, 37, 1], [12, 39, 1], [12, 42, 1], [12, 61, 1], [12, 68, 1], [12, 83, 1], [12, 90, 1], [13, 16, 1], [13, 19, 1], [13, 25, 1], [13, 35, 1], [13, 40, 1], [13, 47, 1], [13, 57, 1], [13, 60, 1], [13, 63, 1], [13, 74, 1], [13, 82, 1], [14, 9, 1], [14, 11, 1], [14, 16, 1], [14, 32, 1], [14, 37, 1], [14, 40, 1], [14, 49, 1], [15, 0, 1], [15, 6, 1], [15, 33, 1], [15, 39, 1], [15, 76, 1], [16, 13, 1], [16, 14, 1], [16, 21, 1], [16, 50, 1], [16, 59, 1], [16, 65, 1], [16, 67, 1], [16, 94, 1], [16, 95, 1], [17, 3, 1], [17, 11, 1], [17, 28, 1], [17, 32, 1], [17, 35, 1], [17, 40, 1], [17, 83, 1], [17, 84, 1], [17, 90, 1], [17, 91, 1], [18, 33, 1], [18, 66, 1], [18, 68, 1], [18, 70, 1], [18, 74, 1], [18, 85, 1], [18, 91, 1], [18, 92, 1], [19, 8, 1], [19, 13, 1], [19, 43, 1], [19, 50, 1], [19, 61, 1], [19, 63, 1], [19, 80, 1], [19, 93, 1], [20, 26, 1], [20, 35, 1], [20, 37, 1], [20, 45, 1], [20, 46, 1], [20, 47, 1], [20, 48, 1], [20, 56, 1], [20, 63, 1], [20, 66, 1], [20, 74, 1], [21, 11, 1], [21, 16, 1], [21, 25, 1], [21, 30, 1], [21, 33, 1], [21, 35, 1], [21, 37, 1], [21, 38, 1], [21, 40, 1], [21, 49, 1], [21, 62, 1], [21, 96, 1], [22, 10, 1], [22, 54, 1], [22, 64, 1], [22, 66, 1], [22, 71, 1], [22, 88, 1], [22, 99, 1], [23, 6, 1], [23, 38, 1], [23, 41, 1], [23, 42, 1], [23, 47, 1], [23, 55, 1], [23, 66, 1], [23, 81, 1], [23, 92, 1], [24, 3, 1], [24, 7, 1], [24, 30, 1], [24, 43, 1], [24, 46, 1], [24, 54, 1], [24, 62, 1], [24, 75, 1], [24, 89, 1], [24, 96, 1], [25, 13, 1], [25, 21, 1], [25, 35, 1], [25, 62, 1], [25, 90, 1], [26, 4, 1], [26, 10, 1], [26, 11, 1], [26, 20, 1], [26, 31, 1], [26, 43, 1], [26, 69, 1], [26, 73, 1], [26, 84, 1], [27, 1, 1], [27, 4, 1], [27, 46, 1], [27, 47, 1], [27, 51, 1], [27, 63, 1], [27, 80, 1], [27, 94, 1], [27, 96, 1], [27, 98, 1], [28, 4, 1], [28, 10, 1], [28, 17, 1], [28, 29, 1], [28, 44, 1], [28, 47, 1], [28, 50, 1], [28, 72, 1], [28, 78, 1], [28, 88, 1], [28, 91, 1], [28, 99, 1], [29, 9, 1], [29, 28, 1], [29, 30, 1], [29, 48, 1], [29, 51, 1], [29, 57, 1], [29, 67, 1], [29, 92, 1], [29, 97, 1], [30, 21, 1], [30, 24, 1], [30, 29, 1], [30, 39, 1], [30, 43, 1], [30, 57, 1], [30, 60, 1], [30, 65, 1], [31, 3, 1], [31, 26, 1], [31, 47, 1], [31, 48, 1], [31, 53, 1], [31, 66, 1], [31, 91, 1], [31, 95, 1], [32, 14, 1], [32, 17, 1], [32, 36, 1], [32, 40, 1], [32, 55, 1], [32, 59, 1], [32, 72, 1], [32, 92, 1], [33, 4, 1], [33, 15, 1], [33, 18, 1], [33, 21, 1], [33, 38, 1], [33, 40, 1], [33, 46, 1], [33, 48, 1], [33, 49, 1], [33, 54, 1], [33, 77, 1], [33, 83, 1], [33, 85, 1], [33, 86, 1], [33, 87, 1], [34, 10, 1], [34, 12, 1], [34, 48, 1], [34, 56, 1], [34, 63, 1], [34, 81, 1], [34, 83, 1], [34, 90, 1], [34, 96, 1], [35, 13, 1], [35, 17, 1], [35, 20, 1], [35, 21, 1], [35, 25, 1], [35, 42, 1], [35, 51, 1], [35, 75, 1], [36, 6, 1], [36, 32, 1], [36, 50, 1], [36, 53, 1], [36, 55, 1], [36, 61, 1], [36, 62, 1], [36, 77, 1], [36, 80, 1], [36, 98, 1], [37, 2, 1], [37, 12, 1], [37, 14, 1], [37, 20, 1], [37, 21, 1], [37, 42, 1], [37, 55, 1], [37, 60, 1], [37, 62, 1], [37, 71, 1], [37, 82, 1], [37, 85, 1], [37, 89, 1], [37, 95, 1], [38, 21, 1], [38, 23, 1], [38, 33, 1], [38, 60, 1], [38, 78, 1], [39, 2, 1], [39, 4, 1], [39, 12, 1], [39, 15, 1], [39, 30, 1], [39, 42, 1], [39, 48, 1], [39, 51, 1], [39, 58, 1], [39, 70, 1], [39, 76, 1], [39, 79, 1], [39, 86, 1], [40, 11, 1], [40, 13, 1], [40, 14, 1], [40, 17, 1], [40, 21, 1], [40, 32, 1], [40, 33, 1], [40, 49, 1], [40, 53, 1], [40, 57, 1], [40, 63, 1], [40, 75, 1], [40, 88, 1], [41, 4, 1], [41, 23, 1], [41, 74, 1], [42, 1, 1], [42, 6, 1], [42, 9, 1], [42, 12, 1], [42, 23, 1], [42, 35, 1], [42, 37, 1], [42, 39, 1], [42, 57, 1], [42, 75, 1], [42, 76, 1], [42, 82, 1], [42, 87, 1], [43, 5, 1], [43, 19, 1], [43, 24, 1], [43, 26, 1], [43, 30, 1], [43, 44, 1], [43, 48, 1], [43, 56, 1], [43, 63, 1], [43, 65, 1], [43, 75, 1], [43, 77, 1], [43, 95, 1], [44, 28, 1], [44, 43, 1], [44, 60, 1], [44, 75, 1], [44, 78, 1], [44, 83, 1], [44, 85, 1], [45, 10, 1], [45, 20, 1], [45, 52, 1], [45, 53, 1], [45, 67, 1], [45, 73, 1], [45, 75, 1], [45, 81, 1], [45, 91, 1], [46, 3, 1], [46, 20, 1], [46, 24, 1], [46, 27, 1], [46, 33, 1], [46, 49, 1], [46, 51, 1], [46, 53, 1], [46, 57, 1], [46, 66, 1], [46, 73, 1], [46, 78, 1], [46, 80, 1], [46, 83, 1], [46, 88, 1], [47, 5, 1], [47, 8, 1], [47, 9, 1], [47, 13, 1], [47, 20, 1], [47, 23, 1], [47, 27, 1], [47, 28, 1], [47, 31, 1], [47, 56, 1], [47, 58, 1], [47, 91, 1], [47, 92, 1], [47, 93, 1], [47, 99, 1], [48, 4, 1], [48, 5, 1], [48, 20, 1], [48, 29, 1], [48, 31, 1], [48, 33, 1], [48, 34, 1], [48, 39, 1], [48, 43, 1], [48, 55, 1], [48, 76, 1], [48, 91, 1], [48, 98, 1], [48, 99, 1], [49, 9, 1], [49, 14, 1], [49, 21, 1], [49, 33, 1], [49, 40, 1], [49, 46, 1], [49, 60, 1], [49, 73, 1], [49, 78, 1], [50, 16, 1], [50, 19, 1], [50, 28, 1], [50, 36, 1], [50, 64, 1], [50, 68, 1], [50, 70, 1], [50, 72, 1], [50, 77, 1], [50, 89, 1], [50, 99, 1], [51, 4, 1], [51, 5, 1], [51, 27, 1], [51, 29, 1], [51, 35, 1], [51, 39, 1], [51, 46, 1], [51, 59, 1], [51, 63, 1], [51, 72, 1], [51, 82, 1], [51, 88, 1], [51, 97, 1], [52, 9, 1], [52, 45, 1], [52, 72, 1], [52, 75, 1], [53, 0, 1], [53, 31, 1], [53, 36, 1], [53, 40, 1], [53, 45, 1], [53, 46, 1], [53, 55, 1], [53, 69, 1], [53, 76, 1], [53, 85, 1], [53, 94, 1], [54, 22, 1], [54, 24, 1], [54, 33, 1], [54, 61, 1], [54, 86, 1], [55, 3, 1], [55, 23, 1], [55, 32, 1], [55, 36, 1], [55, 37, 1], [55, 48, 1], [55, 53, 1], [55, 61, 1], [55, 67, 1], [55, 94, 1], [56, 20, 1], [56, 34, 1], [56, 43, 1], [56, 47, 1], [56, 60, 1], [56, 61, 1], [56, 68, 1], [56, 70, 1], [56, 73, 1], [56, 86, 1], [57, 13, 1], [57, 29, 1], [57, 30, 1], [57, 40, 1], [57, 42, 1], [57, 46, 1], [57, 58, 1], [57, 61, 1], [57, 71, 1], [57, 78, 1], [57, 81, 1], [57, 89, 1], [57, 91, 1], [57, 95, 1], [58, 11, 1], [58, 39, 1], [58, 47, 1], [58, 57, 1], [58, 62, 1], [58, 68, 1], [58, 75, 1], [58, 91, 1], [58, 96, 1], [58, 98, 1], [59, 16, 1], [59, 32, 1], [59, 51, 1], [59, 61, 1], [59, 65, 1], [60, 2, 1], [60, 4, 1], [60, 5, 1], [60, 6, 1], [60, 13, 1], [60, 30, 1], [60, 37, 1], [60, 38, 1], [60, 44, 1], [60, 49, 1], [60, 56, 1], [60, 79, 1], [60, 80, 1], [60, 83, 1], [61, 5, 1], [61, 6, 1], [61, 10, 1], [61, 12, 1], [61, 19, 1], [61, 36, 1], [61, 54, 1], [61, 55, 1], [61, 56, 1], [61, 57, 1], [61, 59, 1], [61, 68, 1], [61, 73, 1], [61, 78, 1], [61, 81, 1], [62, 3, 1], [62, 8, 1], [62, 21, 1], [62, 24, 1], [62, 25, 1], [62, 36, 1], [62, 37, 1], [62, 58, 1], [62, 66, 1], [62, 80, 1], [62, 85, 1], [62, 87, 1], [63, 11, 1], [63, 13, 1], [63, 19, 1], [63, 20, 1], [63, 27, 1], [63, 34, 1], [63, 40, 1], [63, 43, 1], [63, 51, 1], [63, 67, 1], [63, 83, 1], [64, 9, 1], [64, 22, 1], [64, 50, 1], [64, 68, 1], [64, 76, 1], [64, 80, 1], [65, 1, 1], [65, 4, 1], [65, 16, 1], [65, 30, 1], [65, 43, 1], [65, 59, 1], [65, 73, 1], [65, 95, 1], [65, 97, 1], [66, 6, 1], [66, 8, 1], [66, 18, 1], [66, 20, 1], [66, 22, 1], [66, 23, 1], [66, 31, 1], [66, 46, 1], [66, 62, 1], [66, 73, 1], [66, 76, 1], [66, 90, 1], [66, 92, 1], [67, 2, 1], [67, 16, 1], [67, 29, 1], [67, 45, 1], [67, 55, 1], [67, 63, 1], [67, 80, 1], [67, 83, 1], [67, 84, 1], [67, 89, 1], [68, 9, 1], [68, 12, 1], [68, 18, 1], [68, 50, 1], [68, 56, 1], [68, 58, 1], [68, 61, 1], [68, 64, 1], [68, 70, 1], [68, 96, 1], [68, 97, 1], [69, 1, 1], [69, 11, 1], [69, 26, 1], [69, 53, 1], [69, 75, 1], [69, 77, 1], [69, 84, 1], [70, 8, 1], [70, 11, 1], [70, 18, 1], [70, 39, 1], [70, 50, 1], [70, 56, 1], [70, 68, 1], [70, 80, 1], [70, 86, 1], [70, 88, 1], [70, 93, 1], [71, 22, 1], [71, 37, 1], [71, 57, 1], [71, 81, 1], [71, 90, 1], [72, 2, 1], [72, 4, 1], [72, 6, 1], [72, 8, 1], [72, 28, 1], [72, 32, 1], [72, 50, 1], [72, 51, 1], [72, 52, 1], [72, 98, 1], [73, 26, 1], [73, 45, 1], [73, 46, 1], [73, 49, 1], [73, 56, 1], [73, 61, 1], [73, 65, 1], [73, 66, 1], [74, 7, 1], [74, 11, 1], [74, 13, 1], [74, 18, 1], [74, 20, 1], [74, 41, 1], [74, 75, 1], [74, 84, 1], [74, 90, 1], [75, 8, 1], [75, 24, 1], [75, 35, 1], [75, 40, 1], [75, 42, 1], [75, 43, 1], [75, 44, 1], [75, 45, 1], [75, 52, 1], [75, 58, 1], [75, 69, 1], [75, 74, 1], [75, 96, 1], [76, 1, 1], [76, 10, 1], [76, 15, 1], [76, 39, 1], [76, 42, 1], [76, 48, 1], [76, 53, 1], [76, 64, 1], [76, 66, 1], [76, 86, 1], [77, 3, 1], [77, 6, 1], [77, 33, 1], [77, 36, 1], [77, 43, 1], [77, 50, 1], [77, 69, 1], [77, 84, 1], [77, 89, 1], [78, 6, 1], [78, 11, 1], [78, 28, 1], [78, 38, 1], [78, 44, 1], [78, 46, 1], [78, 49, 1], [78, 57, 1], [78, 61, 1], [78, 91, 1], [78, 94, 1], [79, 3, 1], [79, 39, 1], [79, 60, 1], [80, 19, 1], [80, 27, 1], [80, 36, 1], [80, 46, 1], [80, 60, 1], [80, 62, 1], [80, 64, 1], [80, 67, 1], [80, 70, 1], [80, 85, 1], [80, 91, 1], [81, 4, 1], [81, 5, 1], [81, 23, 1], [81, 34, 1], [81, 45, 1], [81, 57, 1], [81, 61, 1], [81, 71, 1], [81, 87, 1], [81, 97, 1], [82, 1, 1], [82, 2, 1], [82, 3, 1], [82, 4, 1], [82, 13, 1], [82, 37, 1], [82, 42, 1], [82, 51, 1], [82, 83, 1], [82, 84, 1], [82, 96, 1], [83, 1, 1], [83, 3, 1], [83, 12, 1], [83, 17, 1], [83, 33, 1], [83, 34, 1], [83, 44, 1], [83, 46, 1], [83, 60, 1], [83, 63, 1], [83, 67, 1], [83, 82, 1], [83, 89, 1], [83, 93, 1], [83, 98, 1], [84, 17, 1], [84, 26, 1], [84, 67, 1], [84, 69, 1], [84, 74, 1], [84, 77, 1], [84, 82, 1], [84, 90, 1], [84, 92, 1], [85, 1, 1], [85, 6, 1], [85, 7, 1], [85, 9, 1], [85, 10, 1], [85, 18, 1], [85, 33, 1], [85, 37, 1], [85, 44, 1], [85, 53, 1], [85, 62, 1], [85, 80, 1], [85, 87, 1], [85, 95, 1], [86, 2, 1], [86, 3, 1], [86, 5, 1], [86, 10, 1], [86, 33, 1], [86, 39, 1], [86, 54, 1], [86, 56, 1], [86, 70, 1], [86, 76, 1], [87, 2, 1], [87, 4, 1], [87, 11, 1], [87, 33, 1], [87, 42, 1], [87, 62, 1], [87, 81, 1], [87, 85, 1], [87, 94, 1], [88, 2, 1], [88, 22, 1], [88, 28, 1], [88, 40, 1], [88, 46, 1], [88, 51, 1], [88, 70, 1], [88, 91, 1], [88, 92, 1], [88, 94, 1], [89, 5, 1], [89, 24, 1], [89, 37, 1], [89, 50, 1], [89, 57, 1], [89, 67, 1], [89, 77, 1], [89, 83, 1], [89, 95, 1], [90, 0, 1], [90, 12, 1], [90, 17, 1], [90, 25, 1], [90, 34, 1], [90, 66, 1], [90, 71, 1], [90, 74, 1], [90, 84, 1], [90, 97, 1], [91, 17, 1], [91, 18, 1], [91, 28, 1], [91, 31, 1], [91, 45, 1], [91, 47, 1], [91, 48, 1], [91, 57, 1], [91, 58, 1], [91, 78, 1], [91, 80, 1], [91, 88, 1], [91, 99, 1], [92, 3, 1], [92, 6, 1], [92, 8, 1], [92, 9, 1], [92, 18, 1], [92, 23, 1], [92, 29, 1], [92, 32, 1], [92, 47, 1], [92, 66, 1], [92, 84, 1], [92, 88, 1], [92, 99, 1], [93, 19, 1], [93, 47, 1], [93, 70, 1], [93, 83, 1], [94, 3, 1], [94, 7, 1], [94, 8, 1], [94, 9, 1], [94, 16, 1], [94, 27, 1], [94, 53, 1], [94, 55, 1], [94, 78, 1], [94, 87, 1], [94, 88, 1], [94, 97, 1], [95, 16, 1], [95, 31, 1], [95, 37, 1], [95, 43, 1], [95, 57, 1], [95, 65, 1], [95, 85, 1], [95, 89, 1], [95, 97, 1], [96, 10, 1], [96, 11, 1], [96, 21, 1], [96, 24, 1], [96, 27, 1], [96, 34, 1], [96, 58, 1], [96, 68, 1], [96, 75, 1], [96, 82, 1], [96, 98, 1], [97, 1, 1], [97, 8, 1], [97, 29, 1], [97, 51, 1], [97, 65, 1], [97, 68, 1], [97, 81, 1], [97, 90, 1], [97, 94, 1], [97, 95, 1], [98, 2, 1], [98, 3, 1], [98, 27, 1], [98, 36, 1], [98, 48, 1], [98, 58, 1], [98, 72, 1], [98, 83, 1], [98, 96, 1], [98, 99, 1], [99, 5, 1], [99, 22, 1], [99, 28, 1], [99, 47, 1], [99, 48, 1], [99, 50, 1], [99, 91, 1], [99, 92, 1], [99, 98, 1]]

matrix_raw = np.zeros((100, 100))
# Loop through the list of tuples and set corresponding positions to 1
for pos in lst:
    row = pos[0]
    col = pos[1]
    val = pos[2]
    matrix_raw[row][col] = val

# Print the matrix
print('this is matrix_raw',matrix_raw)


# Save the full matrix to a text file
np.savetxt("full_matrix.txt", matrix_raw, fmt="%d")

matrix2 = -np.array(matrix_raw)

#matrix = -np.array([
  #              [0, 0, 0, 1, 0],
   #             [0, 0, 1, 1, 1],
    #            [0, 1, 0, 1, 1],
     #           [1, 1, 1, 0, 0],
      #          [0, 1, 1, 0, 0],
       #      ])

# 20 spin MAXCUT problem
N = 100
mc_id = 1 # select first example of 20 spin MAXCUT problem
#J = - np.load(instance_path_str_MAXCUT + f"MC50_N={N}_{mc_id}.npz") # load J matrix for 50% density MAX-CUT problem
gamma = 0.010 # set gamma hyperparameter

#test = Ising(matrix2).solve(cac_gamma=gamma, hyperparameters_randomtune = False)


#print("Time Elapsed: {} seconds".format(test.result.time))
#print("Minimum Energy Achieved: {}".format(test.result.lowest_energy))
#np.set_printoptions(threshold=10, edgeitems=1)
#print("Energy Evolution: {}".format(test.result.energy_evolution))
#print("Spin Evolution: {}".format(test.result.spin_trajectories))
#test.result.plot_spin_trajectories(plot_type="spins")
#test.result.plot_spin_trajectories(plot_type="energy")

timestep_count = 1000
my_feedback_schedule = lambda x: np.sin(x/20)#torch.sin(torch.arange(timestep_count))
#test = Ising(matrix2).solve(cac_gamma=gamma, num_runs=5, num_timesteps_per_run = timestep_count, custom_feedback_schedule=my_feedback_schedule, #hyperparameters_randomtune = False)

#timestep_count = 5000
#ground_state_ising_energy = -29.0
#my_feedback_schedule = lambda x: np.sin(x/33)
#test = Ising(matrix2).solve(cac_gamma=gamma, num_runs=5, target_energy=ground_state_ising_energy, num_timesteps_per_run = timestep_count,
#                      custom_feedback_schedule=my_feedback_schedule, hyperparameters_randomtune = False)

#print(f"Number of discrete steps (roundtrips): {timestep_count}")
#roundtrip_time = 1.6e-6 #Roundtrip time in seconds, as reported in (https://doi.org/10.1126/science.aah5178)
#print(f"Roundtrip time: {roundtrip_time} second")
#print(f"Total CIM runtime: {timestep_count*roundtrip_time} second(s)")




def num_cut_edges(initial_matrix, ground_state_solution):
    num_edges = 0
    for i in range(len(initial_matrix)):
        for j in range(i+1, len(initial_matrix)):
            if initial_matrix[i][j] == 1 and ground_state_solution[i]*ground_state_solution[j] == -1:
                num_edges += 1
    return num_edges

#num_edges = num_cut_edges(matrix_raw, best_cut)

#print("Number of cut edges: ", num_edges)

# Create an empty array
my_array = []

final_time=0

for i in range(1000):
    start_time = time.perf_counter()
    test = Ising(matrix2).solve(cac_gamma=gamma, num_runs=1, num_timesteps_per_run = timestep_count, custom_feedback_schedule=my_feedback_schedule)
    best_cut = test.result.lowest_energy_spin_config


    num_edges = num_cut_edges(matrix_raw, best_cut)
    final_time = time.perf_counter() - start_time 

    my_array.append((num_edges, final_time))


my_array = np.array(my_array)

# Save the array as a NumPy array locally
np.save('my_array.npy', my_array)


# Save the array as a text file
np.savetxt('my_array.txt', my_array) 

print("my_array ", my_array)


print("Number of cut edges: ", num_edges)


# Extract the x and y coordinates from the array of tuples
x = my_array[:, 0]
y = my_array[:, 1]

# Plot the points
plt.scatter(x, y)
plt.xlabel('# cuts ')
plt.ylabel('time in seconds')

# Calculate the average of the y-coordinates
average_x = np.mean(x)

average_y = np.mean(y)

# Print the average of the y-coordinates
print("The average of the x-axis values is:", average_x)

print("The average of the y-axis values is:", average_y)


# Show the plot
plt.show()