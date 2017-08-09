import os, sys

from flogmodel.model import FuzzyLogicModel

from sparql_process.controllers.performance_controller import Performance

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
	print("---->Main")

	performance = Performance()

	#performance.get_latency_times()
	#performance.process_one_user()
	performance.process_two_users()
	#performance.process_eight_users()