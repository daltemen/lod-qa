from flogmodel.model import FuzzyLogicModel

from controllers.dataset_controller import Dataset
from controllers.language_controller import LanguageCheck
from controllers.performance_controller import Performance



class Evaluator:
	"""
	Evaluators for determine 
	A value for each antecedent of the model
	"""
	def __init__(self):
		self.performance = Performance()
		self.language = LanguageCheck()

	def send_to_model(self):
		print("Evaluating Model-------->")
		with open('QUALITY_OUTPUT.txt', 'w') as outfile:

			latency = self.evaluate_latency()
			scalability = self.evaluate_scalability()
			syntactic_validaty = self.language.get_errors_from_dataset()
			trustworthiness = self.evaluate_trustworthiness_from_dataset()
			#TODO: method for evaluate timeliness
			#fake value temporal
			timeliness = self.evaluate_trustworthiness_from_dataset()

			quality_list = []

			for l,sc,sy,tr,ti in zip(
				latency, scalability,
				syntactic_validaty, trustworthiness,
				timeliness
				):

				fuzzy_logic = FuzzyLogicModel(l,
							sc, sy,
							tr, ti
							)
				quality_list.append(fuzzy_logic.get_output())

			outfile.write(','.join(map(str, quality_list)))


	def evaluate_latency(self):
		self.performance.get_latency_times()
		file = open('latency_times.txt', 'r')
		result = file.read().split(',')

		return result

	def evaluate_scalability(self):
		#TODO: Programming the scalability logic

		self.performance.process_one_user()
		#self.performance.process_two_users()
		#self.performance.process_eight_users()
		file = open('one_users.txt', 'r')
		result = file.read().split(',')

		return result

	def evaluate_trustworthiness_from_dataset(self):
		with open('trustworthiness.txt', 'w') as outfile:
			dataset = Dataset()
			dataset_list = dataset.get_creators()
			description_dataset = ''
			trust_values_list = []
			trust_value = 1
			for item in dataset_list:
				trust_values_list.append(trust_value)

			outfile.write(','.join(map(str, trust_values_list)))

		return trust_values_list

