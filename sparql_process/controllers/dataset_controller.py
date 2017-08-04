import json
import pprint

from query_data import data_experimental, data_experimental_getty
from constants import DATASETS


class Dataset:

	def __init__(self):
		self.datasets = DATASETS_LIGHT

	def get_title(self):
		results = results_list()
		titles = []
		for item in results:
			titles.append(item.get('title'))

		return titles

	def get_creators(self):
		results = results_list()
		creators = []
		for item in results:
			creators.append(item.get('creator'))

		return creators, others

	def get_issued_and_modified(self):
		results = results_list()
		issued_list = []
		modified_list = []
		for item in results:
			issued_list.append(item.get('issued'))
			modified_list.append(item.get('modified'))

		return issued_list, modified_list

	def get_descriptions(self):
		results = results_list()
		descriptions_list = []
		for item in results:
			descriptions_list.append(item.get('description'))

		return descriptions_list

	def results_list(self):
		dataset_dict = convert_datasets_as_dict(self)
		return dataset_dict['results']['bindings']

	def convert_datasets_as_dict(self):
		return json.loads(self.datasets)
