#is statement

def return_true():
    return ""

def return_false():
    return ""

if return_true():
    print('True')

if return_false():
    print('False')
else:
    print('else exec')

if return_false():
    pass
elif return_true():
    print('elif exec')
else:
    print('else exec')


# if assignment operator

var1 = 'a' if 3<1 else 'b'
print(var1)
print('****************E1***************')
#Exercitiu Tema:

# def FuncTem():
#     numar = int(input("Numar: "))
#     if numar <3:
#         print('Too small')
#     elif numar==3:
#         print('Just right')
#     else:
#         print("Too big")
# FuncTem()

print('***************L********************')

#loopy loops

# tuple = (1,2,3)
# iterabil = tuple.__iter__()
# print(iterabil.__next__())
# print(next(iterabil))
# print(next(iterabil))
# #print(next(iterabil))

# print(iterabil)
#
# for var in tuple:
#     print(var)
#     if var == 2:
#         break
# else:
#     print('end of for')

#EX2
print("*******************E2****************")

def StrFunc():
    var = input("Give me a string:")
    for x in var:
        if x == 'a':
            print("The string has A's")
            break
        else:
            print("No A's, sorry")
            break

# StrFunc()

print("*******************W****************")
#While

# while True:
#     print('i am lost')
#     break
#
# counter = 0
# while counter <5:
#     print('i am lost')
#     if counter == 5:
#         break
#     counter += 1
#
# else:
#     print("Nu merge, something fucky")

print('**********************E3****************')



def a_in_str():
    prop = input("String:")
    for x in prop:
        if x == 'a':
            print("The str has A's")
            return False
    else:
        return True


def astr():
    while a_in_str():
        pass
# astr()

print("**********************E4*********************")
#instance
# print(isinstance('a', str))

# tuple1= (1, 'a', ('b', 1+1j))
# def find_complex(tuple1):
#     for var in tuple1:
#         print('am un numar: ', var)
#         if isinstance(var, complex):
#             return var
#         if isinstance(var, tuple):
#             for var1 in var:
#                 if isinstance(var1, complex):
#                     print(var1)
#                     return var1
#     else:
#         return False
# find_complex(tuple1)


tuple1= (1, 'a', ('b', 1+1j))

def find_complex(tuple1):
        for var in tuple1:
            print('am un numar: ', var)
            if isinstance(var, complex):
                return var
            if isinstance(var, tuple):
                result = find_complex(var)
                if result is not False:
                    return result
        else:
            return False
# print(find_complex(tuple1))

print('***************************E5**********************')

tuple2= (((True,),),)

def print_bool(tuple2):
    for var in tuple2:
        print('am un obiect: ', var)
        if isinstance(var, tuple):
            print_bool(var)

print_bool(tuple2)