#!/usr/bin/env python

import thinkstats

def main (name, data_dir='.'):
	# Initialisation
	data = [1, 2, 3, 4, 5, 6]

	# Mean, variance
	mean, var = thinkstats.MeanVar(data)

	#
	print 'mu = ' + str(mean) + ', sigma2 = ' + str(var)

if __name__ == '__main__':
	import sys
	main (*sys.argv)

