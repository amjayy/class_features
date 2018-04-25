#class
class Person(object):
    def __init__(self,name):#what it inherits from
        self.name = name#intialize the parameters

    def reveal_identity(self):
        print("My name is {}".format(self.name))

class SuperHero(Person): #inherits from class
    def __init__(self,name,hero_name):
        super(SuperHero, self).__init__(name)#intialize 
        self.hero_name = hero_name

    def reveal_identity(self):
        super(SuperHero,self).reveal_identity()
        print("...And I am {}".format(self.hero_name))
#taking a person class and giving it a name with method reveal.identity
#amber = Person('Amber')#creating an instant of a class
#amber.reveal_identity()

#how to overide a method
#comment out above to overide method
#add in addtional functionality
kawaii = SuperHero('Static Sunflower', 'SS')
kawaii.reveal_identity()
