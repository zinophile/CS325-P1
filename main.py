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

	for idx in range(leng)):
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
