import numpy as np

import skfuzzy as fuzz
from skfuzzy import control as ctrl

SCALE = 1

class FuzzyLogicModel:
	"""
		Input Variables
		+SCALE for visulize in graph
	"""
	latency = ctrl.Antecedent(np.arange(0, 52+SCALE, 1), 'Latency')
	scalability = ctrl.Antecedent(np.arange(1, 10+SCALE, 1), 'Scalability')
	syntactic_validaty = ctrl.Antecedent(np.arange(
		0, 54+SCALE, 1), 'Syntactic Validaty'
	)
	trustworthiness = ctrl.Antecedent(np.arange(
		-1, 1+SCALE, 0.1), 'Trustworthiness'
	)
	timeliness = ctrl.Antecedent(np.arange(0, 1+SCALE, 0.1), 'Timeliness')

	#Output Variable
	quality = ctrl.Antecedent(np.arange(0, 1+SCALE, 0.1), 'Quality')


	def draw_graph(self):
		
		#latency
		self.latency['increased_latency'] = fuzz.trimf(
			self.latency.universe, [0, 53, 100]
		)
		self.latency['decreased_latency'] = fuzz.trimf(
			self.latency.universe, [0, 0, 53]
		)

		#scalability
		self.scalability['low_scalability'] = fuzz.trimf(
			self.scalability.universe, [0, 0, 2]
		)

		self.scalability['medium_scalability'] = fuzz.trimf(
			self.scalability.universe, [0, 2, 8]
		)

		self.scalability['high_scalability'] = fuzz.trimf(
			self.scalability.universe, [2, 8, 9]
		)

		#syntactic_validaty
		self.syntactic_validaty['low_syntactic_validaty'] = fuzz.trimf(
			self.syntactic_validaty.universe, [0, 0, 10]
		)

		self.syntactic_validaty['medium_syntactic_validaty'] = fuzz.trimf(
			self.syntactic_validaty.universe, [0, 36, 54]
		)

		self.syntactic_validaty['high_syntactic_validaty'] = fuzz.trimf(
			self.syntactic_validaty.universe, [36, 54, 55]
		)

		#trustworthiness
		self.trustworthiness['absolute_distrust'] = fuzz.trimf(
			self.trustworthiness.universe, [0, -1, 0]
		)

		self.trustworthiness['absence'] = fuzz.trimf(
			self.trustworthiness.universe, [-1, 0, 1]
		)

		self.trustworthiness['absolute_trust'] = fuzz.trimf(
			self.trustworthiness.universe, [0, 1, 2]
		)

		#timeliness
		self.timeliness['uncertainty'] = fuzz.trimf(
			self.timeliness.universe, [0, 1, 2]
		)
		self.timeliness['certainty'] = fuzz.trimf(
			self.timeliness.universe, [0, 0, 1]
		)

		#output quality
		self.quality['low_quality'] = fuzz.trimf(
			self.quality.universe, [0, 0, 50]
		)

		self.quality['medium_quality'] = fuzz.trimf(
			self.quality.universe, [0, 50, 100]
		)

		self.quality['high_quality'] = fuzz.trimf(
			self.quality.universe, [50, 100, 101]
		)


		increased_latency = self.latency['increased_latency']
		decreased_latency = self.latency['decreased_latency']

		low_scalability = self.scalability['low_scalability']
		medium_scalability = self.scalability['medium_scalability']
		high_scalability = self.scalability['high_scalability']

		low_syntactic_validaty = self.scalability['low_syntactic_validaty']
		medium_syntactic_validaty = self.scalability[
			'medium_syntactic_validaty'
		]
		high_syntactic_validaty = self.scalability['high_syntactic_validaty']

		absolute_distrust = self.trustworthiness['absolute_distrust']
		absence = self.trustworthiness['absence']
		absolute_trust = self.trustworthiness['absolute_trust']

		uncertainty = self.timeliness['uncertainty']
		certainty = self.timeliness['certainty']

		low_quality = self.quality['low_quality']
		medium_quality = self.quality['medium_quality']
		high_quality = self.quality['high_quality']

	def generate_method(self, cont):
		pass