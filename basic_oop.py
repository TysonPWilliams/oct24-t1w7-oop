# Class - blueprint for creating objects- custom data type

# if we're writing code and want to come and give our class a proper body at a later date we can just write 'pass' in the body for now

class Car: # Pascal case - eg. HelloThere
    # Constructor - optional special method that set up attributes of a new instance
    # will be called automatically when a new instance is created

    def __init__(self, make, model, engine): # self is passed implicitly by the interpreter 
        # create an attribute of the newly created object called 'make' and copy the value of the 'make' param into it
        # dunder makes the attr private
        self.__make = make  # dot notation - <object>.<attr/method>
        self.model = model
        self.engine = engine
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


# Inheritance - "is a" relationship. 
class PetrolCar(Car):

    def __init__(self, make, model, engine, tank_capacity_litres):
        super().__init__(make, model, engine) # super() is used to enter the super class (parent) and use what has been previously defined in that parent class.
        self.tank_capacity_litres = tank_capacity_litres

    def __str__(self):
        return f'{super().__str__()}. It has a {self.tank_capacity_litres}L tank.'



# Composition - "has a" relationship
class Engine:
    def __init__(self, type, max_power_kW):
        self.type = type
        self.max_power_kW = max_power_kW

    def __str__(self):
        return f'This is a {self.type} engine with a maximum power of {self.max_power_kW}kW!'




# Main
engine1 = Engine(type='petrol', max_power_kW=235)
my_car = PetrolCar(make='Honda', model='Civic', tank_capacity_litres=47, engine=engine1) # create a new instance of Car
# my_car is now an object of class 'Car'
# your_car = Car(make='Mitsubishi', model='ASX')
# print(my_car.__dict__) # useful for debugging but only developmental purposes, not for live code

# my_car.start()
# your_car.start()
# print(my_car.make)
print(my_car)
# print(your_car)
# your_car.start()
print(engine1)

# print(my_car.get_make())