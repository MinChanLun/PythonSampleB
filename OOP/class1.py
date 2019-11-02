class DogFamily:


	def __init__(self, name, age, Gender):
		self.name = name
		self.age = age
		self.Gender = Gender
		print('(Initizlized DogMember: {}'.format(self.name))

	def bark(self):
		print('Name:"{}"  Age:"{}"  Gender:"{}"'.format(self.name, self.age, self.Gender), end="")


class Shamoyed(DogFamily):
	def __init__(self, name, age, Gender, puppy):
		DogFamily.__init__(self, name, age, Gender)
		self.puppy = puppy
		print('(Initialized DogFamily:"{}")'.format(self.name))


	def bark(self):
		DogFamily.bark(self)
		print(' puppy:"{}"'.format( self.puppy))
		

class GoldenRetiever(DogFamily):
	def __init__(self, name, age, Gender, puppy):
		DogFamily.__init__(self, name, age, Gender)
		self.puppy = puppy
		print('(Initialized DogFamily:"{}")'.format(self.name))


	def bark(self):
		DogFamily.bark(self)
		print(' puppy:"{}"'.format(self.puppy))
		


class Huskey(DogFamily):
	def __init__(self, name, age, Gender, puppy ):
		DogFamily.__init__(self, name, age, Gender)
		self.puppy = puppy
		print('(Initialized DogFamily:"{}")'.format(self.name))


	def bark(self):
		DogFamily.bark(self)
		print(' puppy:"{}"'.format(self.puppy))
		


s = Shamoyed('Shamoyed', 4, 'Female', 4)
g = GoldenRetiever('GoldenRetiever', 3, 'Male', 2)
h = Huskey('Huskey', 6, 'Female', 2)



print()


dogfamily = [s, g, h]
for dog in dogfamily:
	dog.bark()
