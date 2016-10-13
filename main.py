#/usr/bin/env python

'''
                      Project 1
  There are four algorithms that will run for
  this program to compare them. These
  algorithms will determine if there is a max.
  Algorithms are based on examples found at
  https://goo.gl/oYh2NL.

  Team Members:
  Darin Etherington
  Osbaldo Esquivel
  Jared Wasinger
'''


'''
            Algorithm 1: Enumeration

  Loop over each pair of indices i,j and
  compute the sum of A[k] from k=i to k=j.
  Keep the best sum you have found so far.
'''

def enumAlgo(arr):
	sumTemp = 0
	sumMax = 0
	small = 0
	large = 0
    idx = 0

	for idx in range(arr)):
		for temp in range(idx,len(arr)):
			sumTemp = 0  #reset temporary sum
			for x in arr[idx:temp+1]:
                #add to sum for this slice
                #of the array
				sumTemp = sumTemp + x
			if sumMax < sumTemp:
				sumMax = sumTemp   #new max
				large = temp
				small = idx
	return sumMax, small, large

'''
    Algorithm 2: Better Enumeration (iteration)

  Notice that in the previous algorithm the same
  sum is computed many times. In particular, notice
  that the sum of A[k] from k=i to k=j can be
  computed from the sum of A[k] from k=i to
  k=j-1 in O(1) time, rather than starting from
  scratch. Write a new version of the first
  algorithm that takes advantage of this obversation.
'''

def enumBetterAlgo(arr):
    sumTemp = 0
    sumMax = 0
    small = 0
    large = 0
    idx = 0

    for idx in range(len(arr)):
        sumTemp = 0   #reset sumTemp
        for temp in range(i,len(arr)):
            sumTemp += arr[temp]  #running sum
            if sumMax < sumTemp:
                sumMax = sumTemp  #new max
                small = idx
                large = temp
        return sumMax, small, large
		
'''
   Algorithm 2: Divide and Conquer
  
	If we split the array into two halves, we know that the maximum subarray will either be:
	
	* contained entirely in the first half
	* contained enitrely in the second half, or
	* made of a suffx of the first half of the subarray and a prefix of the second half
	
	Algorithm
	
	- Divide the array into two halves
	- Make a recursive call on the left half to find the max sum subarray on that side
   - Make a recursive call on the right half to find the max sum subarray on that side
	- Find the max sum subarray that includes the mid element
			- Find the max sum subarray crossing over to the left
			- Find the max sum subarray crossing over to the right 
	- Return the maximum max sum subarray of the three
	
	STILL TO DO:
	Update code to return max sum subarray indices.
	
'''

def divAndConAlgo(array):		# main function
	first = 0
	last = len(array)
	sumMax = 0
	mid = 0
	
	if len(array) == 1:		# base case, only 1 array element
		sumMax = array[0]
		return sumMax
		
	else
		mid = (first + last) // 2		# // is floor division?
		
		return max(divAndConAlgo(array, first, mid),
					   divAndConAlgo(array, (mid + 1), last),
						maxCrossMidSum(array, first, mid, last))
		# ^^^ can I do this in Python syntax wise, over 3 lines?

		def maxCrossMidSum (array, first, mid, last)
	leftSumTemp = 0
	RightSumTemp = 0
	leftSum = -10000
   rightSum = -10000
	
	for idx in range(mid, first, -1):
		leftSumTemp = leftSumTemp + array[idx]
   
	if leftSumTemp > leftSum:
      leftSum = leftSumTemp
		
   for idx in range(mid, last):
		rightSumTemp = rightSumTemp + array[idx]
   
	if rightSumTemp > rightSum:
      rightSum = rightSumTemp
	
	return leftSum + rightSum
	
'''
   Algorithm 4: Linear-time
  
	This is just Kadane's algorithm.  I adjusted it to return the max sum subarray indices.
	
	Algorithm
	
	Still to write
	
'''

def linearTimeAlgo(array):
	sumMaxEndingHere = array[0]
	sumMax = array[0]
	startIndex = 0
	startIndexTemp = 0
	endIndex = 0
	
	if len(array) == 1:		# base case, only 1 array element
		sumMax = array[0]
		return sumMax
		
	for idx in range(len(array)):
		sumMaxEndingHere = max(0, (sumMaxEndingHere + idx))
		
		if sumMaxEndingHere == 0:
			startIndexTemp = idx + 1
		
		else:
			startIndex = startIndexTemp
			endIndex = idx
			sumMax = sumMaxEndingHere
			#sumMax = max(sumMax, sumMaxEndingHere)

	return startIndex, endIndex, sumMax
