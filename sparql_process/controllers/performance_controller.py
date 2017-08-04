import timeit
import requests

from constants import REQUEST_PERFORMANCE


class Performance:

	def __init__(self):
		self.url = REQUEST_PERFORMANCE
		self.iterador = 2

	def get_latency_times(self):
		times = []
		count = 0
		for i in range(self.iterador):
			count += 1
			start_latency = timeit.default_timer()
			try:
				r = requests.get(self.url)
				print("satisfactory request No {}".format(count))
			except:
				print("request No {} fail".format(count))

			final_latency = timeit.default_timer()
			time_latency = final_latency - start_latency
			times.append(time_latency)

		return times

	def get_scalability_times(self):
		pass