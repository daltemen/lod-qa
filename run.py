import os, sys

from flogmodel.model import FuzzyLogicModel
from sparql_process.controllers.execute_queries import test
from sparql_process.controllers.query_data import data

#FuzzyLogicModel.show_graphs()

#Test values

latency = 25
scalability = 6
syntactic_validaty = 12 
trustworthiness = 0.5
timeliness = 0.7

execute_model = False
sparql_processes = True

if execute_model:
	fuzzy_instance = FuzzyLogicModel(latency,
						scalability, syntactic_validaty,
						trustworthiness, timeliness
						)
	print ("Quality is", fuzzy_instance.get_output())

if sparql_processes:
	#execute_syntactic_validity()
	print(data)