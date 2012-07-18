#!/usr/bin/env python

import Pmf

def main(name, data_dir='.'):
	# Initialisation
	data = [1, 2, 2, 3, 5]

	# Histogram
	hist = Pmf.MakeHistFromList (data)
	print hist.Values()
	for val, freq in hist.Items():
		print val, freq

	# Plot
	import matplotlib.pyplot as pyplot

	vals, freqs = hist.Render()
	rectangles = pyplot.bar (vals, freqs)
	pyplot.show()

if __name__ == '__main__':
	import sys
	main (*sys.argv)

