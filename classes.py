import datetime

class Book:

    def __init__(self):
        # Establish the properties of each book
        # with a default value
        self.title = ""
        self.publisher = ""
        self.author = ""
        self.current_page = 1
        self.year_published = 0
        self.currently_reading = False

    def start_reading(self):
        self.currently_reading = True
        print(f'You start reading {self.title} at page {self.current_page}')

    def stop_reading(self, page):
        self.current_page = page

mockingbird = Book()
mockingbird.title = "To Kill a Mocking Bird"
mockingbird.publisher = "Penguin Books"
mockingbird.author = "Harper Lee"
mockingbird.year_published = "1960"

for prop, value in mockingbird.__dict__.items():
    print(f'{prop}:\n{value}\n')

mockingbird.start_reading()
print(mockingbird.currently_reading)
mockingbird.stop_reading(42)
mockingbird.start_reading()
mockingbird.stop_reading(95)
mockingbird.start_reading()


# Practice: Pizza Joint
class Pizza:

    def __init__(self):
        self.size = "",
        self.crust = "",
        self.toppings = []


    def print_order(self):
        s = " and "
        print(f"I would like to order a {self.size}, {self.crust} pizza with {s.join(self.toppings)} on it.")


deepdish = Pizza()
deepdish.size = "16 inch"
deepdish.crust = "deepdish"
deepdish.toppings = ["pepperoni", "olives", "sausage"]
deepdish.print_order()


# Practice: Companies and Employees
class Employee:
    def __init__(self, name, job_title, start_date):
        self.name = name
        self.job_title = job_title
        self.start_date = start_date

class Company:
    def __init__(self, bus_name, address, industry):
        self.bus_name = bus_name
        self.address = address
        self.industry = industry
        self.employees = list()

    def __str__(self):
        new_hire = list()
        for emp in self.employees:
            new_hire.append(f"\n   *{emp.name}")
        return f"{self.bus_name} is a business in the {self.industry} industry, and its employees are: {' '.join(new_hire)}"

shirt_guys = Company("Shirts for Dirts", "123 Main", "Industry of Shirts")
coffee_girls = Company("El Coffee House", "321 Side", "Industry of Coffee")

adam = Employee("Adam Knowles", "Seamstress", "8/20/2019")
drew = Employee("Drew Palapoza", "Barista", "8/21/2019")
sam = Employee("Sam Birky", "Water Boy", "8/22/2019")
sydney = Employee("Sydney Sydney", "Mop Master", "8/23/2019")
jake = Employee("Jake Scott", "Electrician", "8/24/2019")

shirt_guys.employees.append(adam)
shirt_guys.employees.append(drew)
shirt_guys.employees.append(sam)
coffee_girls.employees.append(sydney)
coffee_girls.employees.append(jake)

print(shirt_guys)
print(coffee_girls)
