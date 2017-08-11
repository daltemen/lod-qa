# -*- coding: utf-8 -*-
import language_check

from dataset_controller import Dataset

class LanguageCheck:

	def __init__(self):
		self.tool = language_check.LanguageTool('en-US')

	def get_errors_from_dataset(self):
		with open('language_checker.txt', 'w') as outfile:

			dataset = Dataset()
			dataset_list = dataset.get_descriptions()
			description_dataset = ''
			number_of_errors = []

			for item in dataset_list:
				description_dataset = item.get('value')
				matches = self.tool.check(description_dataset)
				number_of_errors.append(len(matches))

			outfile.write(','.join(map(str, number_of_errors)))
		return number_of_errors
