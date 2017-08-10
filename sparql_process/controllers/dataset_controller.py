import json
import pprint

from constants import DATASETS


class Dataset:

	def __init__(self):
		self.datasets = DATASETS

	def get_title(self):
		results = self.results_list()
		titles = []
		for item in results:
			titles.append(item.get('title'))

		return titles

	def get_creators(self):
		results = self.results_list()
		creators = []
		for item in results:
			creators.append(item.get('creator'))

		return creators, others

	def get_issued_and_modified(self):
		results = self.results_list()
		issued_list = []
		modified_list = []
		for item in results:
			issued_list.append(item.get('issued'))
			modified_list.append(item.get('modified'))

		return issued_list, modified_list

	def get_descriptions(self):
		results = self.results_list()
		descriptions_list = []
		for item in results:
			descriptions_list.append(item.get('description'))

		return descriptions_list

	def results_list(self):
		dataset_dict = self.convert_datasets_as_dict()
		return dataset_dict['results']['bindings']

	def convert_datasets_as_dict(self):
		return json.loads(self.datasets)