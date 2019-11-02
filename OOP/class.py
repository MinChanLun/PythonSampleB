# class SchoolMember:


# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
# 		print('(Initizlized SchoolMember: {}'.format(self.name))


# 	def tell(self):
# 		print('Name:"{}" Age:"{}"'.format(self.name, self.age), end="")


# class Teacher(SchoolMember):
# 	def __init__(self, name, age, marks):
# 		SchoolMember.__init__(self, name, age)
# 		self.marks = marks #အပေါ်မှာမပါတဲ့ category အသစ်ထပ်ထည့်ဖို့အတွက်သုံးလို့ရတယ်
# 		print('(Initialized Student:{})'.format(self.name))

# 	def tell(self): #အပေါ်မှာမပါတဲ့ category အသစ်ထပ်ထည့်ဖို့အတွက်သုံးလို့ရတယ်
# 		SchoolMember.tell(self)
# 		print('Marks: "{:d}"'.format(self.marks))


# class Student(SchoolMember):
# 	def __init__(self, name, age, marks):
# 		SchoolMember.__init__(self, name, age)
# 		self.marks = marks
# 		print('(Initialized Student:{})'.format(self.name))

# 	def tell(self):
# 		SchoolMember.tell(self)
# 		print('Marks: "{:d}"'.format(self.marks))


# class Headmaster(SchoolMember):
# 	def __init__(self, name, age, marks):
# 		SchoolMember.__init__(self, name, age)
# 		self.marks = marks
# 		print('(Initialized Student:{})'.format(self.name))

# 	def tell(self):
# 		SchoolMember.tell(self)
# 		print('Marks: "{:d}"'.format(self.marks))

class DogFamily:


	def __init__(self, name, age, sex, child):
		self.name = name
		self.age = age
		self.Gender = Gender
		self.puppy = puppy
		print('(Initizlized DogMember: {}'.format(self.name))


		def bark(self):
		DogFamily.bark(self)
		print('Name:"{}" Age:"{}" sex:"{}" puppy:"{}"'.format(self.name, self.age, self.sex, self.child), end="")


class Shamoyed(DogMember):
	def __init__(self, name, age, sex, child ):
		DogFamily.__init__(self, name, age, Gender, puppy)
		#Category တွေအကုန်ပါနေလို့မထည့်လည်းရ။

class GoldenRetiever(DogMember):
	def __init__(self, name, age, sex, child ):
		DogFamily.__init__(self, name, age, Gender, puppy)


class Huskey(DogMember):
	def __init__(self, name, age, sex, child ):
		DogFamily.__init__(self, name, age, Gender, puppy)


	# def tell(self):
	# 	dog.tell(self)
	# 	print('Name:"{:d}" Age:"{:d}" sex:"{:d}" child:"{:d}"'.format(self.name, self.age, self.sex, self.child), end="")



# t = Teacher('Mrs. Shrividya', 40, 30000)
# s = Student('Swaroop', 25, 75)
# h = Headmaster('U Tan Daing', 60, 100)
s = Shamoyed('Shamoyed', 4, Female, 4)
g = GoldenRetiever('GoldenRetiever', 3, Male, 2)
h = Huskey('Huskey', 6, Female, 2)



# print()


# members = [t, s, h]
# for member in members:
# 	member.tell()
	



dogs = [s, g, h]
for dog in dogfamily:
	dog.bark()


