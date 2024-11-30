# Class - blueprint for creating objects- custom data type

# if we're writing code and want to come and give our class a proper body at a later date we can just write 'pass' in the body for now

class Car: # Pascal case - eg. HelloThere
    # Constructor - optional special method that set up attributes of a new instance
    # will be called automatically when a new instance is created

    def __init__(self, make, model): # self is passed implicitly by the interpreter 
        # create an attribute of the newly created object called 'make' and copy the value of the 'make' param into it
        # dunder makes the attr private
        self.__make = make  # dot notation - <object>.<attr/method>
        self.model = model
        # implicitly returns self

    def start(self):
        print(f'{self.__make} {self.model} started!')

    # Function overloading - not supported in Python

    def __str__(self): # Returns a string representation of the object
        return f'This is a {self.__make} {self.model}.'
    
    # Getter
    def get_make(self):
        # Authorise to see if user can get it
        # if condition 
        return self.__make
        # side-effects
    
    # Setter
    def set_make(self, new_make):
        # Validate new_make 
        # Authorise 
        self.__make = new_make


class PetrolCar(Car):

    def __init__(self, make, model, tank_capacity_litres):
        super().__init__(make, model) # super() is used to enter the super class (parent) and use what has been previously defined in that parent class.
        self.tank_capacity_litres = tank_capacity_litres

    def __str__(self):
        return f'{super().__str__()}. It has a {self.tank_capacity_litres}L tank.'


# Main
my_car = PetrolCar('Honda', 'Civic', 47) # create a new instance of Car
# my_car is now an object of class 'Car'
your_car = Car('Mitsubishi', 'ASX')
# print(my_car.__dict__) # useful for debugging but only developmental purposes, not for live code
# print(your_car)
# my_car.start()
# your_car.start()
# print(my_car.make)
print(my_car)
print(your_car)
# your_car.start()

# print(my_car.get_make())