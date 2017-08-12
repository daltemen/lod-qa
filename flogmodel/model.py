import numpy as np

import skfuzzy as fuzz
from skfuzzy import control as ctrl

SCALE = 1

class FuzzyLogicModel:
	"""
		Input Variables
		+SCALE for visulize in graph
	"""

	def __init__(self, latency, scalability,
		syntactic_validaty,	trustworthiness,
		timeliness):

		self.latency = latency
		self.scalability = scalability
		self.syntactic_validaty = syntactic_validaty
		self.trustworthiness = trustworthiness
		self.timeliness = timeliness

	def get_output(self):

		print "--> get_output"

		rules = self.get_rules()
		tipping_ctrl = ctrl.ControlSystem(rules)
		tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

		tipping.input['latency'] = self.latency
		tipping.input['scalability'] = self.scalability
		tipping.input['syntactic_validaty'] = self.syntactic_validaty
		tipping.input['trustworthiness'] = self.trustworthiness
		tipping.input['timeliness'] = self.timeliness

		tipping.compute()
		return tipping.output['quality']

	def get_rules(self):

		print "--> get_rules"

		inputs_outputs, graphs = self.get_model()

		#Latency Rules
		rule_1 = ctrl.Rule(
			inputs_outputs.get('increased_latency') &
			inputs_outputs.get('high_scalability') &
			inputs_outputs.get('certainty'),
			inputs_outputs.get('high_quality')
			)

		rule_2 = ctrl.Rule(
			inputs_outputs.get('decreased_latency') &
			inputs_outputs.get('low_scalability'),
			inputs_outputs.get('medium_quality')
			)

		rule_3 = ctrl.Rule(
			inputs_outputs.get('increased_latency') &
			inputs_outputs.get('low_scalability') &
			inputs_outputs.get('uncertainty'),
			inputs_outputs.get('low_quality')
			)

		#Scalability Rules
		rule_4 = ctrl.Rule(
			inputs_outputs.get('high_scalability') &
			inputs_outputs.get('certainty'),
			inputs_outputs.get('high_quality')
			)

		rule_5 = ctrl.Rule(
			inputs_outputs.get('medium_scalability') &
			inputs_outputs.get('low_syntactic_validaty') &
			inputs_outputs.get('absolute_trust') ,
			inputs_outputs.get('medium_quality')
			)

		rule_6 = ctrl.Rule(
			inputs_outputs.get('low_scalability') &
			inputs_outputs.get('uncertainty'),
			inputs_outputs.get('low_quality')
			)

		#Syntactic Validity Rules
		rule_7 = ctrl.Rule(
			inputs_outputs.get('low_syntactic_validaty') &
			inputs_outputs.get('absolute_trust'),
			inputs_outputs.get('high_quality')
			)

		rule_8 = ctrl.Rule(
			inputs_outputs.get('medium_syntactic_validaty') &
			inputs_outputs.get('certainty'),
			inputs_outputs.get('medium_quality')
			)

		rule_9 = ctrl.Rule(
			inputs_outputs.get('high_syntactic_validaty') &
			inputs_outputs.get('increased_latency') &
			inputs_outputs.get('uncertainty'),
			inputs_outputs.get('low_quality')
			)

		#Trustworthiness Rules
		rule_10 = ctrl.Rule(
			inputs_outputs.get('absolute_trust') &
			inputs_outputs.get('decreased_latency') &
			inputs_outputs.get('low_syntactic_validaty'),
			inputs_outputs.get('high_quality')
			)

		rule_11 = ctrl.Rule(
			inputs_outputs.get('absolute_trust') &
			inputs_outputs.get('medium_syntactic_validaty'),
			inputs_outputs.get('medium_quality')
			)

		rule_12 = ctrl.Rule(
			inputs_outputs.get('absolute_distrust'),
			inputs_outputs.get('low_quality')
			)

		#Timeliness Rules
		rule_13 = ctrl.Rule(
			inputs_outputs.get('certainty') &
			inputs_outputs.get('decreased_latency'),
			inputs_outputs.get('high_quality')
			)

		rule_14 = ctrl.Rule(
			inputs_outputs.get('certainty') &
			inputs_outputs.get('medium_syntactic_validaty') |
			inputs_outputs.get('absolute_trust'),
			inputs_outputs.get('medium_quality')
			)

		rule_15 = ctrl.Rule(
			inputs_outputs.get('uncertainty') &
			inputs_outputs.get('absolute_distrust') &
			inputs_outputs.get('high_syntactic_validaty'),
			inputs_outputs.get('low_quality')
			)
		return [
			rule_1, rule_2, rule_3,
			rule_4,	rule_5, rule_6,
			rule_7, rule_8,	rule_9,
			rule_10, rule_12, rule_13,
			rule_14, rule_15]


	def get_model(self):
		print "----> get model"

		latency = ctrl.Antecedent(np.arange(0, 43+SCALE, 1), 'latency')
		scalability = ctrl.Antecedent(np.arange(1, 116, 1), 'scalability')
		syntactic_validaty = ctrl.Antecedent(np.arange(
			0, 54+SCALE, 1), 'syntactic_validaty')

		trustworthiness = ctrl.Antecedent(np.arange(
			-1, 1+SCALE, 0.1), 'trustworthiness')

		timeliness = ctrl.Antecedent(np.arange(0, SCALE, 0.1), 'timeliness')

		#Output Variable
		# Consequent
		quality = ctrl.Consequent(np.arange(0, 99+SCALE, 1), 'quality')

		#latency
		latency['increased_latency'] = fuzz.trimf(
			latency.universe, [0, 43, 100])

		latency['decreased_latency'] = fuzz.trimf(
			latency.universe, [0, 0, 43])

		#scalability
		scalability['high_scalability'] = fuzz.trimf(
			scalability.universe, [0, 0, 33])

		scalability['medium_scalability'] = fuzz.trimf(
			scalability.universe, [0, 33, 115])

		scalability['low_scalability'] = fuzz.trimf(
			scalability.universe, [34, 115, 116])

		#syntactic_validaty
		syntactic_validaty['low_syntactic_validaty'] = fuzz.trimf(
			syntactic_validaty.universe, [0, 0, 10])

		syntactic_validaty['medium_syntactic_validaty'] = fuzz.trimf(
			syntactic_validaty.universe, [0, 36, 54])

		syntactic_validaty['high_syntactic_validaty'] = fuzz.trimf(
			syntactic_validaty.universe, [36, 54, 55])

		#trustworthiness
		trustworthiness['absolute_distrust'] = fuzz.trimf(
			trustworthiness.universe, [-2, -1, 0])

		trustworthiness['absence'] = fuzz.trimf(
			trustworthiness.universe, [-1, 0, 1])

		trustworthiness['absolute_trust'] = fuzz.trimf(
			trustworthiness.universe, [0, 1, 2])

		#timeliness
		timeliness['uncertainty'] = fuzz.trimf(
			timeliness.universe, [0, 1, 2])

		timeliness['certainty'] = fuzz.trimf(
			timeliness.universe, [0, 0, 1])

		#output quality
		quality['low_quality'] = fuzz.trimf(
			quality.universe, [0, 0, 50])

		quality['medium_quality'] = fuzz.trimf(
			quality.universe, [0, 50, 100])

		quality['high_quality'] = fuzz.trimf(
			quality.universe, [50, 100, 101])

		i_o = {
				'increased_latency': latency['increased_latency'],
				'decreased_latency': latency['decreased_latency'],
				'low_scalability' : scalability['low_scalability'],
				'medium_scalability' : scalability['medium_scalability'],
				'high_scalability' : scalability['high_scalability'],
				'low_syntactic_validaty' : syntactic_validaty['low_syntactic_validaty'],
				'medium_syntactic_validaty': syntactic_validaty['medium_syntactic_validaty'],
				'high_syntactic_validaty': syntactic_validaty['high_syntactic_validaty'],
				'absolute_distrust': trustworthiness['absolute_distrust'],
				'absence': trustworthiness['absence'],
				'absolute_trust': trustworthiness['absolute_trust'],
				'uncertainty': timeliness['uncertainty'],
				'certainty': timeliness['certainty'],
				'low_quality': quality['low_quality'],
				'medium_quality': quality['medium_quality'],
				'high_quality': quality['high_quality']
			}

		return i_o, [
			latency, scalability,
			syntactic_validaty, trustworthiness,
			timeliness, quality
			]

	def show_graphs(self):
		print "----> Show graphs"
		i_o, graphs = self.get_model()

		for var in graphs:
			var.view()

		raw_input("Press a key...")
		exit()
