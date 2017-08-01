import os, sys

from flmodel.model import FuzzyLogicModel


#FuzzyLogicModel.show_graphs()

#Test values

latency = 25
scalability = 6
syntactic_validaty = 12 
trustworthiness = 0.5
timeliness = 0.7

#
fuzzy_instance = FuzzyLogicModel(latency,
					scalability, syntactic_validaty,
					trustworthiness, timeliness
					)

#Method for show graphs .show_graphs()


#Method for processing quality
print ("Quality is", fuzzy_instance.get_output())

