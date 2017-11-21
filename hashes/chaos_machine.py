"""example of simple chaos machine"""


class ChaosMachine():
	def __init__(self):
		self.K= [0.33, 0.44, 0.55, 0.44, 0.33]
		self.t = 3
		self.m = 5
		self.buffer_space = self.K
		self.params_space = [0]*self.m
		self.machine_time = 0

	def push(self, seed):

		# Choosing Dynamical Systems (All)
		for key, value in enumerate(self.buffer_space):
			# Evolution Parameter
			e = float(seed / value)

			# Control Theory: Orbit Change
			value = (self.buffer_space[(key + 1) % self.m] + e) % 1

			# Control Theory: Trajectory Change
			r = (self.params_space[key] + e) % 1 + 3

			# Modification (Transition Function) - Jumps
			self.buffer_space[key] = \
			  round(float(r * value * (1 - value)), 10)
			self.params_space[key] = \
			  r # Saving to Parameters Space

		# Logistic Map
		assert(max(self.buffer_space) < 1)
		assert(max(self.params_space) < 4)

		# Machine Time
		self.machine_time += 1

	def pull(self):

	  # PRNG (Xorshift by George Marsaglia)
		def xorshift(X, Y):
			X ^= Y >> 13
			Y ^= X << 17
			X ^= Y >> 5
			return X

	  # Choosing Dynamical Systems (Increment)
		key = self.machine_time % self.m

		# Evolution (Time Length)
		for i in range(0, self.t):
			# Variables (Position + Parameters)
			r     = self.params_space[key]
			value = self.buffer_space[key]

		# Modification (Transition Function) - Flow
		self.buffer_space[key] = \
		  round(float(r * value * (1 - value)), 10)
		self.params_space[key] = \
		  (self.machine_time * 0.01 + r * 1.01) % 1 + 3

		# Choosing Chaotic Data
		X = int(self.buffer_space[(key + 2) % self.m] * (10 ** 10))
		Y = int(self.buffer_space[(key - 2) % self.m] * (10 ** 10))

		# Machine Time
		self.machine_time += 1

		return xorshift(X, Y) % 0xFFFFFFFF


#######################################

if __name__ == "__main__":
	# Initialization
	machine = ChaosMachine()

	# Pushing Data (Input)
	import random
	message = random.sample(range(0xFFFFFFFF), 100)
	for chunk in message:
	  machine.push(chunk)

	# Pulling Data (Output)
	# while True:
	for i in range(100):
	  print("%s" % format(machine.pull(), '#04x'))
	  print(machine.buffer_space); print(machine.params_space)
