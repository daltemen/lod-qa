from datetime import datetime

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
		self.dataset = Dataset()
		self.performance = Performance()
		self.language = LanguageCheck()

	def send_to_model(self):
		latency = self.evaluate_latency()
		scalability = self.evaluate_scalability()
		syntactic_validaty = self.language.get_errors_from_dataset()
		trustworthiness = self.evaluate_trustworthiness_from_dataset()
		timeliness = self.evaluate_timeliness()

		quality_list = []
		print("Evaluating Model-------->")
		with open('QUALITY_OUTPUT.txt', 'w') as outfile:
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
		print("evaluating latency...")
		self.performance.get_latency_times()
		file = open('latency_times.txt', 'r')
		result = file.read().split(',')

		return result

	def evaluate_scalability(self):
		print("evaluating scalability...")
		self.performance.process_one_user()
		self.performance.process_eight_users()
		file_one = open('one_users.txt', 'r')
		result_one = [float(x) for x in file_one.read().split(",")]

		list_of_lists = []
		count = 0
		for i in range(8):
			count += 1
			file = open('eight_users_{}.txt'.format(count),'r')
			read = [float(x) for x in file.read().split(",")]
			list_of_lists.append(read)

		sum_list = [sum(item) for item in zip(*list_of_lists)]
		divide_list = [i/8 for i in sum_list]
		result_list = [i/j for i,j in zip(result_one,divide_list)]

		return result_list

	def evaluate_trustworthiness_from_dataset(self):
		print("evaluating trustworthiness...")
		with open('trustworthiness.txt', 'w') as outfile:
			dataset_list = self.dataset.get_creators()
			description_dataset = ''
			trust_values_list = []
			trust_value = 1
			for item in dataset_list:
				trust_values_list.append(trust_value)

			outfile.write(','.join(map(str, trust_values_list)))

		return trust_values_list

	def evaluate_timeliness(self):
		print("evaluating timeliness...")
		dataset_issue, dataset_modified = self.dataset.get_issued_and_modified()
		
		result_list = []
		# (current - modified) / (current - issued)
		for i, m in zip(dataset_issue, dataset_modified):
			result_list.append(
				(datetime.today().year - int(datetime.strptime(m['value'],
					'%Y-%m-%d+%H:%M').strftime('%Y'))
				) / 
				(datetime.today().year - int(datetime.strptime(i['value'],
					'%Y-%m-%d+%H:%M').strftime('%Y')))
			)

		return result_list