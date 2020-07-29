colour = 'green'
colour = 'red'
print(colour)

class Car(object):
    """ My first class """

    def __init__(self):
        self.color =  'red'

    def __str__(self):
        self.color = 'green'
        return 'this is the class string'

    def paint_car(self):
        self.color = 'green'

my_car = Car()
print(type(my_car))
print(my_car.__doc__)
print(my_car.color)
print(my_car.__str__())
print(my_car.paint_car())
print(my_car.color)

print("*"*50, "E2" , "*"*50)

# instance variables
class Wolf():

    def __init__(self):
        print('wolf')
        self.has_pack = True
        print('###', self.breed)

    def bark(self):
        print('woof')

class Dogs(Wolf):

    def __init__(self, breed ):  #overload
        print('dog')
        self.breed = breed
        super().__init__()


dog = Dogs(breed = 'Husky')
print(dog.breed)
print(dog.has_pack)





print("*"*50, "#class variables" , "*"*50)

# data = 1
# def test_data():
#     if data:
#         print("We have data!")
#
# test_data()
#
# class SportCars:
#     color = "white"
#
#     def __init__(self, color):
#         print(color)
#         print(self.color)
#         self.color = color
#
# s_car = SportCars('blue')


# s_car.color
print("*"*50, "#class variable issue" , "*"*50)

class Fruits:
    colors = ["white"]

    def __init__(self):
        print(id(self.colors))

fruit1 = Fruits()
print(id(Fruits.colors))
fruit1.colors.append('pink')
print(id(fruit1.colors))
print(Fruits.colors)
fruit2 = Fruits()
print(fruit2.colors)

print("*"*50, "#E4 decode-encode" , "*"*50)

import communicator
text = "Text to encode"
secret = communicator.MySecret()
encode_text = secret.encode(text)
print(encode_text)
print(len(encode_text))

secret2 = communicator.MySecret()
decoded_text = secret2.decode(encode_text)
print(decoded_text)
print(len(decoded_text))


print("*"*50, "### variables (global, non-local, local)" , "*"*50)

global_var = 'a'

def func1():
    global global_var
    global_var = 'b'
    local_var = 'c'

    def func2():
        nonlocal local_var
        local_var = 'd'
        print("non-local in func2", local_var)

    func2()
    print("local in func1:", local_var)
    print("global in func1", global_var)

func1()
print("after func", global_var)

print("*"*50, "### exemplu mostenire)" , "*"*50)


class A():
    def methond_a(self):
        print('a')

class B(A):
    def methond_a(self):
        print('b')

    def methond_b(self):
        print('b1')

class C(B, A):
    pass
    # def methond_a(self):
    #     print('c')


c = C()

c.methond_a()
c.methond_b()

print("*"*50, "E5", "*"*50)

# from communicator import Client
#
# client = Client(prime=3, base=7)
# print(client.prime, client.base)
#
# from communicator import Server
#
# server = Server(prime=13, base=19)
# print(server.prime, server.base)


# print("*"*50, "Prime", "*"*50)
# def prime(limit_inf, limit_sup):
#     prime_list = []
#     for i in range(limit_inf,limit_sup):
#         for j in range (2, i//2):
#             if i%j == 0:
#                 break
#         else:
#             prime_list.append(i)
#     return prime_list
# # print(prime(128, 255))
#

print("*"*50, "Exceptions", "*"*50)

a = 1
class OtherMathError(ArithmeticError):
    ex_info = 'math data'
    def __init__(self, *args, **kwargs):
        print(args)


try:
    if a:
        raise OtherMathError('This is my math error')
    else:
        0/0
except OtherMathError as error:
    print(error.ex_info)
    print('This is something else')
except ZeroDivisionError as e:
    raise e
    print('Not a good number')
except ArithmeticError:
    print('Other math error')

except:
    print(0)
print("*"*50, "Exceptions2", "*"*50)



class MyNewException(Exception):
    def __init__(self, *args, **kwargs):
        print(args[0][::-1])
        super().__init__(args[1:],kwargs)



try:
    raise MyNewException('Test data', 'New data')
except MyNewException as exception:
    print(exception)


#lambda functions
print("*"*50, "Lambda", "*"*50)

var1 = lambda a, b: a+b
print(type(var1(1,2)))

def math_calc(func1,number):
    return (3*func1(number)+1)**(1/2)

print(math_calc(lambda x : x*3,2))


a = 2
b = 3

def ridicare_la_putere(x,y, z):

    return (x+y)/z(a,b)

print(ridicare_la_putere(2,3, lambda a,b:a**b))



