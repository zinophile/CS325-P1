#!/usr/bin/env python

'''
   Algorithm 4: Linear-time
  
	This is just Kadane's algorithm.  I adjusted it to return the max sum subarray indices.
	
	Algorithm
	
	Still to write
	
'''

def linearTimeAlgo(array):
	sumMaxEndingHere = 0
	sumMax = 0
	startIndex = 0
	startIndexTemp = 0
	endIndex = 0
	
	if len(array) == 1:		# base case, only 1 array element
		sumMax = array[0]
		#print array
		#print sumMax
		return startIndex, endIndex, sumMax
	
	else:	
		for idx, val in enumerate(array):
			if (sumMaxEndingHere + val) > 0:
				sumMaxEndingHere = sumMaxEndingHere + val
		
			else:
				sumMaxEndingHere = 0
				startIndexTemp = idx + 1
				
			if sumMaxEndingHere > sumMax:
				sumMax = sumMaxEndingHere
				startIndex = startIndexTemp
				endIndex = idx + 1
				#sumMax = max(sumMax, sumMaxEndingHere)
	
		#print array[startIndex:endIndex]
		#print sumMax
		return startIndex, endIndex, sumMax

def main():
	array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
	print array
	
	startIndex, endIndex, sumMax = linearTimeAlgo(array)
	
	if startIndex == endIndex:
		print array
	else:
		print array[startIndex:endIndex]
	
	print sumMax
	print
	
if __name__ == "__main__":
	main()