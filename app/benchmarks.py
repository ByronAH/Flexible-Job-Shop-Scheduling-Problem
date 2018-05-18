from customparser import parse
from geneticscheduler import GeneticScheduler

from colorama import init
from termcolor import colored

import copy
import numpy as np
import timeit


class Benchmarks:
	def __init__(self, path):
		init()  # Init colorama for color display
		self.__size = list(set(np.logspace(0, 2, num=10, dtype=np.int)))
		self.__name = path.split('/')[-1].split('.')[0]
		self.__jobs_list, self.__machines_list, self.__number_max_operations = parse(path)

	# Plot a 2d graph
	@staticmethod
	def plot2d(filename, xdata, ydata, title, xlabel, ylabel):
		import matplotlib.pyplot as plt
		plt.clf()
		plot = plt.subplot()
		plot.set_title(title)
		plot.set_xlabel(xlabel)
		plot.set_ylabel(ylabel)
		plot.plot(xdata, ydata)
		plot.autoscale()
		plt.show()
		plt.savefig(filename, bbox_inches='tight')

	# Plot a 3d graph
	@staticmethod
	def plot3d(filename, xdata, ydata, zdata, title, xlabel, ylabel, zlabel):
		from mpl_toolkits.mplot3d import Axes3D
		import matplotlib.pyplot as plt

		plt.clf()
		fig = plt.figure()
		plot = fig.gca(projection='3d')
		plot.set_title(title)
		plot.set_xlabel(xlabel)
		plot.set_ylabel(ylabel)
		plot.set_zlabel(zlabel)
		plot.scatter(xdata, ydata, zdata, c='b', marker='o')
		plot.autoscale()
		plt.show()
		plt.savefig(filename, bbox_inches='tight')

	# Benchmarks the genetic scheduler when we increase total population
	def population(self):
		benchmarks_population = []

		print(colored("[BENCHMARKS]", "yellow"), "Gathering computation time for different population sizes")
		for size in self.__size:
			print(colored("[BENCHMARKS]", "yellow"), "Current population size =", size)
			start = timeit.default_timer()
			temp_machines_list, temp_jobs_list = copy.deepcopy(self.__machines_list), copy.deepcopy(self.__jobs_list)
			s = GeneticScheduler(temp_machines_list, temp_jobs_list)
			total_time = s.run_genetic(total_population=size, max_generation=100, verbose=False)
			stop = timeit.default_timer()
			print(colored("[BENCHMARKS]", "yellow"), "Done in", stop - start, "seconds")
			benchmarks_population.append((size, 100, stop - start, total_time))
			del temp_machines_list, temp_jobs_list
		print(colored("[BENCHMARKS]", "yellow"), "Gathering for different population sizes completed")

		self.plot2d(self.__name + "_benchmarks_population", [element[0] for element in benchmarks_population],
					[element[2] for element in benchmarks_population],
					"Time as a function of population size for " + self.__name + " (100 generations)",
					"Population size", "Time (in seconds)")

		return benchmarks_population

	# Benchmarks the genetic scheduler when we increase total population
	def generation(self):
		benchmarks_generation = []

		print(colored("[BENCHMARKS]", "yellow"), "Gathering computation time for different generation numbers")
		for size in self.__size:
			print(colored("[BENCHMARKS]", "yellow"), "Current max generation =", size)
			start = timeit.default_timer()
			temp_machines_list, temp_jobs_list = copy.deepcopy(self.__machines_list), copy.deepcopy(
				self.__jobs_list)
			s = GeneticScheduler(temp_machines_list, temp_jobs_list)
			total_time = s.run_genetic(total_population=100, max_generation=size, verbose=False)
			stop = timeit.default_timer()
			print(colored("[BENCHMARKS]", "yellow"), "Done in", stop - start, "seconds")
			benchmarks_generation.append((100, size, stop - start, total_time))
			del temp_machines_list, temp_jobs_list
		print(colored("[BENCHMARKS]", "yellow"), "Gathering for different population sizes completed")

		self.plot2d(self.__name + "_benchmarks_generation", [element[1] for element in benchmarks_generation],
					[element[2] for element in benchmarks_generation],
					"Time as a function of max generation for " + self.__name + " (100 individuals)", "Max generation",
					"Time (in seconds)")

		return benchmarks_generation

	# Benchmarks 3d

	def run(self):
		benchmarks_population = self.population()
		self.plot3d(self.__name + "_benchmarks_population_with_time", [element[0] for element in benchmarks_population],
					[element[1] for element in benchmarks_population],
					[element[3] for element in benchmarks_population],
					"Best time found as a function of population size and max generation", "Population size",
					"Max generation", "Total time")
# benchmarks_generation = self.generation()