class Student:
    no_of_projects = 1

    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

    def detail(self):
        return f"Name is {self.name}. Age is {self.age}. Role is {self.role}"
    @classmethod
    def changeProjects(cls, projects):
        cls.no_of_projects = projects

    @classmethod
    def from_string_by_pip_dash(cls, str):
        return cls(*str.split("-||-"))

    @classmethod
    def from_string_by_colon(cls,str):
        return cls(*str.split(":"))
    pass


# chirag = Student()
# chirag.name = "Chirag"
# chirag.age = 22
# chirag.role = "Developer"
# print(chirag.__dict__)
# print(Student.__dict__)
# chirag.no_of_projects = 11
# print(chirag.__dict__)

"""
Class with prop and mathod and constructor or __init__
"""

# chirag = Student("Chirag", 22, "Developer")
# friends = Student("FCOMPANY", 34, "CEO")
# print(friends.no_of_projects, "Default Value")
# friends.no_of_projects = 11
# print(friends.no_of_projects, "Change Value")
# # For Class variable value change
# print(Student.no_of_projects, "Class")
# chirag.changeProjects(12)
# print(Student.no_of_projects, "Class")
# print(chirag.no_of_projects, "Instance")
# print(chirag.detail())


"""
Class with alternative constructor
"""
friends = Student.from_string_by_pip_dash("FCOMPANY-||-34-||-CEO")
print(friends.__dict__)

newfriends = Student.from_string_by_colon("NCOMPANY:35:GTA-CEO")
print(newfriends.__dict__)