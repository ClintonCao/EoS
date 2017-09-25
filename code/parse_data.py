import pandas as pd
import pylab as pl
import numpy as np


def read_file(file_name ='../data/export2.csv' ,colomns =None):
	#read dataframe object for cls and could return only certain columns if desired
	if colomns is not None:
		return pd.read_csv(file_name, usecols = colomns)
	else:
		return pd.read_csv(file_name)

def distinct_counter(df, column_name):
	#Given a column it will calculate all the disctint items
	column = df[column_name]
	column_counter = {}
	for item in column:
		if item not in column_counter:
			column_counter[item] = 1
		else:
			column_counter[item] += 1

	return column_counter

def bar_chart_dictionary(dct):
	#makes a barchart from all the items in the dictionary
	X = np.arange(len(dct))
	pl.bar(X, dct.values(), align='center', width=.25)
	pl.xticks(X, dct.keys())
	ymax = max(dct.values()) + 1
	pl.ylim(0, ymax)
	pl.show()


df = read_file()
locations_counter = distinct_counter(df,"Location")
bar_chart_dictionary(locations_counter)
