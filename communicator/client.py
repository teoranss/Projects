from communicator import MySecret
from util import prime
from random import randint

class Client(MySecret):
    def __init__(self, base):
        primes = prime(128,256)
        len(primes)
        number_of_primes = len(primes)
        rand_element1 =randint(0, number_of_primes)
        rand_element2 =randint(rand_element1 +1, number_of_primes)

        self.prime = prime[rand_element1]
        self.base = primes[rand_element2]