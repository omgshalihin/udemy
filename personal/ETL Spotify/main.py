from mimetypes import init


def return_random(value):
    return value

print(return_random('two'))




def return_two():
    return "two"

print(return_two())





class Dog:
    def __init__(self):
        pass
    
    def bark(self):
        return "bark bark bark bark bark bark..."

d = Dog()
apple = d.bark()
print(apple)




def add(a, b = 10):
    return a + b

c = add(20)
print(c)



ingredients = ['caster sugar', 
               'double cream', 
               'butter', 
               'glucose syrup', 
               'vanilla bean paste']

ingredients = tuple(ingredients)

print(type(ingredients))

def number_squared(x):
    print(x ** 2)
  
number_squared(3)

car = {'brand':'Ferrari','model':'model','year':2019}
a = type(car)
print(a)

x = 99.9
print(type(x))


class Planet:
    def __init__(self, name):
        self.name = name       
v = Planet('venus')
test = v.name
print(test)



numbers = [9, 2, 5, 11, 4, 3]
smallest = min(numbers)
print(smallest)

class Planet:
    def __init__(self, name, diameter_km):
        self.name = name
        self.diameter_km = diameter_km
        
e = Planet('Earth', 12742)
test2 = e.name 
test3 = e.diameter_km
print(test2)
print(test3)


a = [i*2 for i in range(5)]
print(a)

i = 0
while i < 5:
  print(i)
  i = i + 1

s = "animal-horse"

a = s.split("-")
print(a)


d = {
    'apple': 1,
    'banana': 2,
    'coconut': 3
}

d['durian'] = 4

print(d)


book = {
    'title': 'The Giver',
    'author': 'Lois Lowry',
    'rating': 4.13
}

book['rating'] = 4.6


a = book['rating']
print(a)

w = 'python'
w_iterator = iter(w)
a = next(w_iterator)
print(a)


def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)

def foo(a, b=4, c=6):
    print(a, b, c)
 
a = foo(20, c=12)

def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)