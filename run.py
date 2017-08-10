import os, sys

from flogmodel.model import FuzzyLogicModel

from sparql_process.controllers.performance_controller import Performance
from sparql_process.controllers.dataset_controller import Dataset
from sparql_process.controllers.language_controller import LanguageCheck
#Test values

latency = 25
scalability = 6
syntactic_validaty = 12
trustworthiness = 0.5
timeliness = 0.7

execute_model = False
sparql_processes = False
evaluator = False
checking = True

if execute_model:
	fuzzy_instance = FuzzyLogicModel(latency,
						scalability, syntactic_validaty,
						trustworthiness, timeliness
						)
	#fuzzy_instance.show_graphs()
	print ("Quality is", fuzzy_instance.get_output())

if sparql_processes:
	#execute_syntactic_validity()
	print("---->Main")

	performance = Performance()

	#performance.get_latency_times()
	#performance.process_one_user()
	performance.process_two_users()
	#performance.process_eight_users()

if evaluator:
	dataset_instance = Dataset()
	print(dataset_instance.get_descriptions())

if checking:
	language_instance = LanguageCheck()
	print(language_instance.get_errors_from_dataset())