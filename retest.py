#!/usr/bin/python

import os, time

time0 = time.time()

#tests = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
#		 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
#		 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
#		 270, 273, 279, 283, 287, 292, 294, 296, 298, 301,
#		 308, 319, 323, 333, 335, 343, 348, 350, 351, 367,
#		 369, 375, 377, 379, 394, 407, 410, 413, 417, 421,
#		 422, 431, 432, 433, 441, 444, 445, 448]

#tests = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
#		 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
#		 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
#		 271, 272, 281, 291, 297, 300, 307, 309, 313, 316,
#		 317, 321, 330, 344, 349, 354, 355, 380, 382, 386,
#		 388, 398, 401, 402, 404, 409, 420, 427, 431, 436]

tests = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
		 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
		 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
		 60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
		 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
		 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
		 270, 271, 272, 273, 279, 281, 283, 287, 291, 292,
		 294, 296, 297, 298, 300, 301, 307, 308, 309, 313,
		 316, 317, 319, 321, 323, 330, 333, 335, 343, 344,
		 348, 349, 350, 351, 354, 355, 367, 369, 375, 377,
		 379, 380, 382, 386, 388, 394, 398, 401, 402, 404,
		 407, 409, 410, 413, 417, 420, 421, 422, 427, 431,
		 432, 433, 436, 441, 444, 445, 458]

for i in tests:
	os.system('node test/math2.js ' + str(i))

time1 = time.time()

print 'Running time:'
print time1 - time0

