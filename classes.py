#9-1
class Resturant:

	def __init__(self, resturant_name, cuisine_type):
		self.resturant_name = resturant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_resturant(self):
		print(f"{self.resturant_name} is a resturant that sells {self.cuisine_type} food, it has server {self.number_served}")

	def open_resturant(self):
		print(f"{self.resturant_name} is open")

	def set_number_served(self, served):
		self.number_served = served
		

	def increment_number_served(self, persons):
		self.number_served += persons


resturant = Resturant('Hooters', 'Americana')
resturant.set_number_served(25)
resturant.increment_number_served(222)


#9-3
class User:

	def __init__(self, first_name, last_name, age, weight):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.weight = weight
		self.login_attempts = 0

	def describe_user(self):
		print(f"{self.first_name} {self.last_name} is a {self.age} who weighs {self.weight}.  You have logged in {self.login_attempts}")

	def greet_user(self):
		print(f"Hi there {self.first_name}")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

person = User('mike', 'landon', 23, 299)
person.increment_login_attempts()
person.increment_login_attempts()
person.increment_login_attempts()
person.increment_login_attempts()

person.describe_user()
