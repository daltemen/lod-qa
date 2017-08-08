import time
from multiprocessing import Process

import timeit
import requests

from constants import REQUEST_PERFORMANCE


class Performance:

	def __init__(self):
		self.url = REQUEST_PERFORMANCE
		self.iterador = 2

	def get_latency_times(self):	
		time_latency = self.request_url_and_time(
				name_file='latency_times')

		return times

	def get_scalability_times(self):
		pass

	def request_url_and_time(self, name_file=None, iterator=2):
		times = []
		count = 0
		for i in range(iterator):
			count += 1
			start_latency = timeit.default_timer()
			try:
				r = requests.get(self.url)
				print("satisfactory request No {}".format(count))
			except Exception as e:
				print(e)
				print("request No {} fail".format(count))

			final_latency = timeit.default_timer()
			time_latency = final_latency - start_latency
			times.append(time_latency)

		return times

	def process_one_user(self):
		p1 = Process(target = self.request_url(
			name_file='two_users_{}'.format(count)
			))
		p1.start()

		while p1.is_alive() == True:
			pass

		print("process_one Finished")

	def process_two_users(self):
		process_list = []
		count = 0
		for i in range(2):
			count += 1
			process = None
			process = Process(target = self.request_url(
				name_file='two_users_{}'.format(count)
				))
			process.start()
			process_list.append(process)

		while all(p.is_alive() == True for p in process_list):
			#not tested
			#time.sleep(1)
			pass

		print("process_two_users Finished")


	def process_eight_users(self):
		process_list = []
		count = 0
		for i in range(8):
			count += 1
			process = None
			process = Process(target = self.request_url(
				name_file='eight_users_{}'.format(count)
				))
			process.start()
			process_list.append(process)

		while all(p.is_alive() == True for p in process_list):
			#not tested
			#time.sleep(1)
			pass

		print("process_eight_users Finished")