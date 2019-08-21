import datetime

"""
Design a program to help keep track of all the students and faculty at a university.
"""

class Person(object):
    def __init__(self, name): 
        """Create a person""" 
        self.name = name
    try:
        lastBlank = name.index(' ')
        self.lastName = name[lastBlank+1:] 
    except:
        self.lastName = name 
    #     self.birthday = None

    def getName(self):
        #"""Returns self's full name""" 
        return self.name
    
    def getLastName(self):
        #"""Returns self's last name""" 
        return self.lastName
    
    def setBirthday(self, birthdate):
        # """Assumes birthdate is of type datetime.date
        # Sets self's birthday to birthdate""" 
        self.birthday = birthdate
    
    def getAge(self):
        # """Returns self's current age in days""" 
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    def __lt__(self, other):
        # """Returns True if self's name is lexicographically
        # less than other's name, and False otherwise""" 
        if self.lastName == other.lastName:
            return self.name < other.name 
        return self.lastName < other.lastName

    def __str__(self):
        # """Returns self's name""" 
        return self.name

me = Person('Michael Guttag')
him = Person('Barack Hussein Obama')
her = Person('Madonna')
print(him)

print(him.getLastName())
him.setBirthday(datetime.date(1961, 8, 4)) 
her.setBirthday(datetime.date(1958, 8, 16))
print(him.getName(), 'is', him.getAge(), 'days old')

class MITPerson(Person):
    nextIdNum = 0 #identification number
    def __init__(self, name): 
        Person.__init__(self, name) 
        self.idNum = MITPerson.nextIdNum 
        MITPerson.nextIdNum += 1
    def getIdNum(self): 
        return self.idNum
    def __lt__(self, other):
        return self.idNum < other.idNum