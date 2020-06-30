# # integers
#
# integ1 = 1
# print(type(integ1))
# print(dir(integ1))
#
# # hex numbers
# hex1 = 0x1f
# print(hex1)
#
# # octal numbers
# oct1 = 0o12
# print(oct1)
#
# # bin numbers
# bin1 = 0b11
# print(bin1)
#
# # write number with exponent
#
# exp1 = 3e4
# print(exp1)
#
# #operators and methods
#
# sum1 = hex1 + oct1
#
# print(sum1)
#
# print(hex1.__add__(oct1))
# print(oct1.__add__(hex1))
#
# div1 = 1/3
# div1 = (1).__truediv__(3)
#
# print(div1)
#
# pow1 = 2**2
# print(pow1)
# pow2 = pow(2,3)
# print(pow2)
#
# # calculate
# a = 3
# b = 4
# c = 5
#
# x = (-b + ((b**2) - 4*a*c)**(1/2)) / (2*a)
# print(x)
#
# # _4ac = 4*a*c
# # b2= pow(b,2)
# # resultRad = b2 - _4ac
# # resultSus = -b +
#
# # x = (-b + pow(b**2 - 4 * a * c, 1/2)) / (2 * a)
#
# # float and complex
#
# float1 = 1.0
# int1 = 1
# complex = 0.2 + 0.1j
# sum_float_int = float1 + int1 + complex
# print(sum_float_int)
#
# #Bool obj
# obj1 = True
# obj2 = False
# obj3 = True
#
# print(id(obj1))
# print(id(obj2))
# print(id(obj3))
#
# #print bool object
# print(type(True))
# print(type(str(True)))
# print(type(True.__str__()))
#
#
# #unary operation
# not1 = not True
# print(not1)
#
# # binary operation
# and1 = False and True or False
#
# print(and1)
#
# #convert to bool
# print(bool(0))
# print(bool(0.0))
# print(bool(0.0 + 0.0j))
# print(bool(''))
# print(bool(False))
# print(''.__len__().__bool__())
# print((0).__bool__())
#
# # None type obj
# none = None
#
#
# # strings
# # string1 = r'ab\n'\
# #           r'c'
# # string2 = """a
# #              b
# #              c"""
# # # print(string1)
# # print(string2)
#
# #adding str
# string1 = 'x'
# string2 = 'y'
# string3 = 'z'
# text = string1 + string2
# print(text)
# text = string1.__add__(string2)
# print(text)
# text = text * 2
# print(text)
# text = text.__mul__(2)
# print(text)
# #order of operations
# print(string1 + string2*3)
#
# # slice
# text = "Hello {}{replace} world"
# print(text[0:5:2])
# print(text[-5:])
#
# #string methods
# formated_text = text.format('abc', replace = 'abc')
# print(formated_text)
#
# #join
# join_text = ' ! '.join([text, text])
# print(join_text)
#
# nr_of_char = len(text)
# print(nr_of_char)
#
# text1 = 'my_text'
# text2 = text1
# text3 = text1[:]
# print((text1==text3))
# print(id(text1))
# print(id(text2))
# print(id(text3))
#
# #Operational
#
# greater = 1<2
# print(greater)
# print(type(greater))
#
# equal = 2 != 2
# print(equal)
# print(type(equal))
#
# #div_by_0 = 0/0
#
# a = 1
# a = a + 1
# print(a)
#
# a = 1
# a += 1
# print(a)
#
# result = 1 < 1.1
# print(result)
#
# #compare strings
# and_str = "a" and "b"
# print(and_str)
# print(and_str == "b")
#
# #result = False and True
#
# or_str = "a" or "b"
# print(or_str)
# print(or_str == "b")
#
# result = True + False + 1
# print(result)
#
# var1 = 1
# var2 = 2
#
# var1, var2 = var2, var1
#
# print(var1)
# print(var2)





#Functions:

def func1():
    print('hello world')
    return None

func1()
func1.__call__()
print(type(func1()))


def func2():
    return 'hello world 2'
result = func2()
print(type(func2()))
print(result)

def func3(text1,text2):
    print(text1, text2, sep='__')

func3('hello', 'wrold')


def func4(text1,text2, x ='None', y='\n'):
    print(text1, text2, sep = x, end = y)
func4('hello', 'world')
func4('hello', 'wrold', ' x ')
func4('hello', 'wrold', y = '\nx\n')

# Tuple
tuple1 = 1, 2, 3
string1 ='1'
tuple2 = '1',
tuple3 = tuple2 + tuple1
print(tuple3)

tuple4 = tuple2 * 4
print(tuple4)

print(type(tuple1))

print('#condese argument')
print("###############")
def func5(*args, **kwargs):
    print(type(kwargs))
    print(len(kwargs))
    print(args[0], args[1], sep = kwargs['x'], end = kwargs['y'])

func5('hello', 'wrold', 'terra', y = '\nx\n', x = '__' )

#homework func

def func6(text1):
    print(text1[::-1])
func6("text inversat")

#bitwise
nr_bin = bin(100)
print(nr_bin)

and_bits = 1 & 2
print(and_bits)

or_bits = 10 | -10
print(or_bits)
print(bin(-0))

# encrypt
print("******************************")

# message = ord("A")
# key = ord("c")
#
# encrypted = message ^ key
# print(chr(encrypted))
# decrypted = encrypted ^ key
# print(chr(decrypted))

#cryptare caractere
# def cryptare(text):
#     key = int(input("Key: "))
#     return ((ord(text[0]) ^ key) + (ord(text[1]) ^ key) + (ord(text[2]) ^ key) + (ord(text[3]) ^ key) + (ord(text[0]) ^ key))
# print(cryptare('12345'))


def crypt(text, key):
    return chr(ord(text[0]) ^ key) + \
           chr(ord(text[1]) ^ key) + \
           chr(ord(text[2]) ^ key)
print(crypt("abc", 7))


