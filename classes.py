#9-1
class Resturant:

	def __init__(self, resturant_name, cuisine_type):
		self.resturant_name = resturant_name
		self.cuisine_type = cuisine_type

	def describe_resturant(self):
		print(f"{self.resturant_name} is a resturant that sells {self.cuisine_type} food")

	def open_resturant(self):
		print(f"{self.resturant_name} is open")

resturant = Resturant('Hooters', 'Americana')
resturant1 = Resturant('Table X', 'Upscale')
resturant2 = Resturant('Mcdonalds', 'Fast Food')

#9-2
resturant.describe_resturant()
resturant1.describe_resturant()
resturant2.describe_resturant()

#9-3
class User:

	def __init__(self, first_name, last_name, age, weight):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.weight = weight

	def describe_user(self):
		print(f"{self.first_name} {self.last_name} is a {self.age} who weighs {self.weight}")

	def greet_user(self):
		print(f"Hi there {self.first_name}")

person = User('mike', 'landon', 23, 299)
person.describe_user()
