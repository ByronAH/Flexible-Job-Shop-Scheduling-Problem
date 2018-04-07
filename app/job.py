class Job:
	def __init__(self, id_job):
		self.__id_job = id_job
		self.__activities_to_be_done = []
		self.__activities_done = []

	# Display the job nicer
	def __str__(self):
		output = ""

		for activity in self.__activities_to_be_done:
			output += str(activity) + "\n"

		for activity in self.__activities_done:
			output += str(activity) + "\n"

		return output

	# Return the job's id
	@property
	def id_job(self):
		return self.__id_job

	# Add an activity to the job
	def add_activity(self, activity):
		self.__activities_to_be_done.append(activity)

	# Return if the job is done
	@property
	def is_done(self):
		return len(self.activities_to_be_done) == 0

	# Return the activities yet to be done
	@property
	def activities_to_be_done(self):
		return self.__activities_to_be_done

	# Return the activities already done
	@property
	def activities_done(self):
		return self.__activities_done

	# Method an activity call to signal it's done
	def activity_is_done(self, activity):
		if not activity.is_done:
			raise EnvironmentError("This activity is not done")
		self.__activities_to_be_done = list(filter(lambda element: element.id_activity != activity.id_activity, self.__activities_to_be_done))
		self.__activities_done.append(activity)

	# Return the current activity that need to be processe
	@property
	def current_activity(self):
		if len(self.activities_to_be_done) == 0:
			raise EnvironmentError("All activities are already done")
		return self.__activities_to_be_done[0]