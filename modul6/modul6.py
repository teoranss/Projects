import time

# generator

my_list = [1, 2, 3]
my_gen = (e for e in my_list)

print(next(my_gen))
print(next(my_gen))
print(next(my_gen))


# print(next(my_gen))

def my_new_gen(my_new_list):
    for element in my_new_list:
        if element > 2:
            yield element + 3
            continue
        yield element * 3


gen1 = my_new_gen(my_list)
print(type(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
# print(next(gen1))

print("*" * 50, "E1", "*" * 50)


def factorial_to_x(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
        yield result


gen2 = factorial_to_x(5)
for _ in range(5):
    print(next(gen2))

print("*" * 50, "E2", "*" * 50)


def my_new_gen2(y):
    result = [y]
    for _ in range(y):
        new_result = result * 100
        for i in new_result:
            result.append(i)
            yield result


gen3 = my_new_gen2(100)
for _ in range(3):
    next(gen3)

print("*" * 50, "E3", "*" * 50)
import random

# def prime(limit_inf, limit_sup):
#     var = random.randint(limit_inf, limit_sup)
#
#     for i in var:
#         for j in range(2, i // 2):
#             if i % j == 0:
#                 break
#         else:
#             yield i
#
# prime_gen = prime(10000, 30000)
#
# for _ in range(2015):
#     next(prime_gen)
# print(next(prime_gen))

print("*" * 50, "Any & All functions", "*" * 50)

var1 = any([0, 1, 2, 3])  # or
print(var1)
var2 = all([0, 1, 2, 3])  # and
print(var2)

print("*" * 50, "Iterators", "*" * 50)

iter_obj = iter([1, 2, 3])
print(type(iter_obj))
print(type(iter_obj.__iter__()))
for i in iter_obj:
    print(i)

try:
    print(next(iter_obj))

except Exception as e:
    pass


class MyIteraror():
    my_data = [1, 2, 3]

    def __str__(self):
        print('I am an iterator')

    def __repr__(self):
        print('I am an interator')

    def __iter__(self):
        return self

    def __next__(self):
        if not len(my_list):
            raise StopIteration
        return my_list.pop(0)


my_iter = MyIteraror()
print(type(my_iter))
print(type(my_iter.__iter__()))

for i in my_iter:
    print(i)

print("*" * 50, "Improved Iterators", "*" * 50)


class MyIteraror():
    my_data = 1

    def __iter__(self):
        return self

    def __next__(self):
        x = self.my_data
        self.my_data = x + 1
        if x < 10:
            return x

        raise StopIteration


my_iter1 = MyIteraror()
print(next(my_iter1))

# for i in my_iter1:
#     print(i)
print("*" * 50, "Improved Iterators E1", "*" * 50)
string1 = 'abc'
obj1 = string1.__iter__()
print('=========================================')
for i in string1:
    print(i)
for i in string1:
    print(i)
print('=========================================')


class MyIterableObject():
    def __iter__(self):
        return MyIteraror()

    def my_test(self):
        print("+++", "+0+", "+++", sep='\n')


my_iterable_object = MyIterableObject()
my_iterable_object.my_test()
for i in my_iterable_object:
    print(i)
for i in my_iterable_object:
    print(i)
print("==============================")


class Prime():
    def __init__(self, lim_inf, lim_sup):
        self.lim_inf = lim_inf
        self.lim_sup = lim_sup
        self.partial_res = None
        self.var = list(range(self.lim_inf, self.lim_sup))

    def __iter__(self):
        return self

    def __next__(self):
        self.partial_res = self.var.pop(0)
        for j in range(2, self.partial_res // 2):
            if self.partial_res % j == 0:
                self.__next__()
        else:
            return self.partial_res


var4 = Prime(128, 256)
print(next(var4))

print("==============Files================")

stream1 = open('C:/Users/admin/PycharmProjects/Projects/modul6/text.txt', mode='rb')
print(type(stream1))
new_read1 = stream1.read()
print(type(new_read1))
print(new_read1)
stream1.close()

stream2 = open('C:/Users/admin/PycharmProjects/Projects/modul6/text.txt', mode='rt')
print(type(stream2))
new_read2 = stream2.read()
print(type(new_read2))
print(new_read2)
stream2.close()

stream3 = open('text.txt', mode='wt')
stream3.write('New Text')
print(type(stream3))
stream3.close()
print("==============E1================")

with open('text.txt', mode='r') as stream4:
    print(stream4.read())

# stream4.__enter__()
# stream4.__exit__()

import time


class Context():
    def __init__(self):
        print('in constructor')
        time.sleep(1)
        # self.sleep = 1

    def __enter__(self):
        print('Before create')
        time.sleep(1)
        # self.sleep = 10
        return self

    def do_some_work(self):
        print('working')
        # time.sleep(self.sleep)

    def __exit__(self, type, value, traceback):
        print(traceback)
        print('after end')
        # time.sleep(1)


# con = Context()
# with con as context:
#     context.do_some_work()
#     raise Exception('some error')


print("==============byte================")

var1 = b'My text'
print(type(var1))
var2 = var1.decode()
print(type(var2))
var3 = var2.encode()
print(type(var3))

print("==============Map Function===============")
a = [1, 2, 3]

map_obj = map(lambda x: x + 1, a)
print(type(map_obj))
for i in map_obj:
    print(i)

a = [1, 2, 3]
b = [3, 3, 3]

map_obj = map(lambda x, y: x + y + 1, a, b)
print(type(map_obj))
for i in map_obj:
    print(i)

animal = ['rabbit', 'tiger', 'human']
mappped_animal = map(lambda s: s if 'g' in s else None, animal)
for i in mappped_animal:
    print(i)

print("============== Filters ===============")

filtered_animals = filter(lambda s: s if 'g' in s else None, animal)
for i in filtered_animals:
    print(i)

print("============== Special Filters ===============")
print("============== All (and) ===============")
print(all([0, 1, 2, 3]))


def my_all(my_iter):
    def my_filter_function(elem):
        return bool(elem)

    for element in my_iter:
        if my_filter_function(element):
            continue
        return False
    else:
        return True


print(my_all([0, 1, 2, 3]))
print("============== Any (or) ===============")

print(any([0, 0, 0, 0]))


def my_any(my_iter2):
    def my_filter_function1(v):
        return bool(v)

    for j in my_iter2:
        if not my_filter_function1(j):
            return True
    else:
        return False


print(my_any([0, 0, 0, 0]))

print("============== Modul 6/curs final ===============")