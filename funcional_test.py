import os, sys

from data_analysis.regresion import show_summary
from flogmodel.model import FuzzyLogicModel
from sparql_process.evaluators import Evaluator

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
dataset = False
checking = False
evaluators = False
analysis = True

if analysis:
	show_summary()

if execute_model:
	fuzzy_instance = FuzzyLogicModel(latency,
						scalability, syntactic_validaty,
						trustworthiness, timeliness
						)
	fuzzy_instance.show_graphs()
	print ("Quality is", fuzzy_instance.get_output())

if sparql_processes:
	#execute_syntactic_validity()
	print("---->Main")

	performance = Performance()
	performance.get_latency_times()
	#performance.process_one_user()
	#performance.process_two_users()
	#performance.process_eight_users()

if dataset:
	dataset_instance = Dataset()
	print(dataset_instance.get_descriptions())
	print(dataset_instance.get_creators())
	print(dataset_instance.get_issued_and_modified())

if checking:
	language_instance = LanguageCheck()
	print(language_instance.get_errors_from_dataset())

if evaluators:
	evaluator = Evaluator()
	print(evaluator.evaluate_timeliness())