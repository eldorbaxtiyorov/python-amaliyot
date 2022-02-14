class Talaba:
    objects = []

    def __init__(self, name, age, level=1):
        self.name = name
        self.__age = age
        self.__level = level
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age > 0 and age < 120:
            self.__age = age
        
    def __str__(self):
        return f"{self.name} {self.age} {self.__level}"

tom = Talaba("Tom", 23)
jack = Talaba(age=23, name='Jack')
print(jack)



tom.age = 12
print(tom)



class Vehicle:
    objects = []
    def __init__(self, model, horse_power, speed):
        self.model = model
        self.horse_power = horse_power
        self.speed = speed
        Vehicle.objects.append(self)
    
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, model):
        if isinstance(model, str):
            self.__model = model
        else:
            self.__model = ''
    @property
    def horse_power(self):
        return self.__horse_power
    @horse_power.setter
    def horse_power(self, horse_power):
        if horse_power > 0  and horse_power < 1000:
            self.__horse_power = horse_power
        else:
            self.__horse_power = 0

    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self, speed):
        if speed > 0 and speed < 1000:
            self.__speed = speed
        else:
            self.__speed = 0
    def move(self, to):
        print(f"Vehicle is going to {to}")

    def __str__(self):
        return f"{self.model} {self.horse_power} {self.speed}"

class Ground(Vehicle):
    objects = []

    def __init__(self, model, horse_power, speed, type, IsPetrol):
        super().__init__(model, horse_power, speed)
        self.type = type
        self.IsPetrol = IsPetrol
        Ground.objects.append(self)
    
    def move(self, to, fro="Samarkand"):
        print(f"Vehicle is going from {fro} to {to}")

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type):
        if isinstance(type, str):
            self.__type = type
        else:
            self.__type = ''
    
    @property
    def IsPetrol(self):
        return self.__IsPetrol

    @IsPetrol.setter
    def IsPetrol(self, IsPetrol):
        if isinstance(IsPetrol, bool):
            self.__IsPetrol = IsPetrol
        else:
            self.__IsPetrol = ''
    
    def __str__(self):
        return super().__str__() + f" {self.type} {self.IsPetrol}"

train = Ground("Telsa", 21, 32, 'train', False)
train.move('Tashkent', "Samarkand")
train.move('Tashkent')


s = "sddskdsj"
print(len(s))



l = [1, 2, 3, 4]
print(len(l))



print(1, 2, 3)
print(1, 2)


def sum(a, b, c=0):
    return a + b + c
print(sum(3, 4))
print(sum(3, 4, 5))



def sum(*a):
    s = 0
    for item in a:
        s += item
    return s
print(sum(1))
print(sum(1, 3))
print(sum(1, 3, 3))



def my_sum(one_required_argument, **kagrs):
    print(type(kagrs))
    print(kagrs)
    s = one_required_argument
    for key, value in kagrs.items():
        print(key, value)
        s += value
    print('s =', s)


#my_sum(1)
my_sum(1, a=2, b=3, c=4)
#my_sum(1, a=2, b=3, c=4, d=5)

