"""
Question 1:Build a program to manage a university's course catalog. You want to define a base class Course that has the
following properties: course_code: a string representing the course code (e.g., "CS101") course_name: a string representing the course name (e.g., "Introduction to Computer Science")
credit_hours: an integer representing the credit hours for the course (e.g., 3)You also want to define two subclasses
CoreCourse and ElectiveCourse, which inherit from the Course class.CoreCourse should have an additional property
required_for_major which is a boolean representing whether the course is required for a particular major. ElectiveCourse should have an additional property elective_type which is a string
representing the type of elective (e.g., "general", "technical", "liberal arts").
"""
# class Course:
#     def __init__(self, course_code, course_name, credit_hours):
#         self.course_code = course_code
#         self.course_name = course_name
#         self.credit_hours = credit_hours
#
# class CoreCourse(Course):
#     def __init__(self, course_code, course_name, credit_hours, required_for_major):
#         Course.__init__(self, course_code, course_name, credit_hours)
#         self.required_for_major = required_for_major
#
# class ElectiveCourse(Course):
#     def __init__(self, course_code, course_name, credit_hours, elective_type):
#         Course.__init__(self, course_code, course_name, credit_hours)
#         self.elective_type = elective_type
#
# cs101=CoreCourse("CS101","Introduction to Computer Science",3,True)
# math202=ElectiveCourse("MATH202","Calculus",4,"general")
#
# print(cs101.course_code)
# print(cs101.course_name)
# print(cs101.credit_hours)
# print(cs101.required_for_major)
# print(math202.course_code)
# print(math202.course_name)
# print(math202.credit_hours)
# print(math202.elective_type)

"""
Question 2: (5 Marks) Create a Python module named employee that contains a class Employee with attributes name, 
salary and methods get_name() and get_salary(). Write a program to use this module to create an object of the 
Employee class and display its name and salary.
"""
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def get_name(self):
#         return self.name
#
#     def get_salary(self):
#         return self.salary
#
# import employee
#
# # Create an object of the Employee class
# emp1 = employee.Employee("Amy", 50000)
# # Display its name and salary
# print("Name:", emp1.get_name())
# print("Salary:", emp1.get_salary())

