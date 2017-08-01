import os, sys
#sys.path.append(os.path.join(os.path.dirname(__file__), "flmodel"))

from flmodel.model import FuzzyLogicModel


#FuzzyLogicModel.show_graphs()

#Test values

latency = 25
scalability = 6
syntactic_validaty = 12 
trustworthiness = 0.5
timeliness = 0.7

print ("Quality is: ",FuzzyLogicModel.get_ouput(
	latency, scalability,
	syntactic_validaty, trustworthiness,
	timeliness
	))