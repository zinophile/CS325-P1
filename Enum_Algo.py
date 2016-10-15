#!/usr/bin/env python

'''
   Algorithm 1: Enumeration
  
	
'''

def enumAlgo(arr):
	sumTemp = 0
	sumMax = 0
	small = 0
	large = 0
   #idx = 0

	for idx in range(0, len(arr)):
		#for temp in range(idx,len(arr)):
		sumTemp = 0  #reset temporary sum
			
		for x in range(idx, len(arr)):
				#add to sum for this slice of the array
			sumTemp = sumTemp + arr[x]
			
			if sumMax < sumTemp:
				sumMax = sumTemp   #new max
				large = x + 1
				small = idx

	return sumMax, small, large

def main():
	array = [5, -4]
	print array
	
	sumMax, small, large = enumAlgo(array)
	
	if small == large:
		print array
	else:
		print array[small:large]
	
	print sumMax
	print
	
if __name__ == "__main__":
	main()