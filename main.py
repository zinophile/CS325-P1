#/usr/bin/python3.2

# ##############################
#                            Project 1                          #
#   There are four algorithms that will run for    #
#    this program to compare them. These        #
#    algorithms will determine if there is a max  #
# ##############################


# ##############################
#                Algorithm 1: Enumeration              #
#  Loop over each pair of indices i,j and            #
#  compute the sum of A[k] from k = i to j.       #
#  Keep the best sum you have found so far      #
#  ##############################
def enumAlgo(arr):
	idx = 0
	sumTemp = 0
	sumMax = 0
	small = 0
	large = 0

	for idx in range(leng)):
		for temp in range(idx,len(arr)):
			sumTemp = 0
			for x in arr[idx:temp+1]:
				sumTemp = sumTemp + x
			if sumMax < sumTemp:
				sumMax = sumTemp
				large = temp
				small = idx
	return sumMax, small, large
	
