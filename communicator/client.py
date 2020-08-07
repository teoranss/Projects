from communicator import MySecret
import time
from util import prime
from random import randint
from socket import socket


class Client(MySecret):
    def __init__(self, base, host, port):
        self.host = host
        self.port = port
        primes = prime(128, 256)
        len(primes)
        number_of_primes = len(primes)
        rand_element1 = randint(0, number_of_primes)
        rand_element2 = randint(rand_element1 + 1, number_of_primes)

        self.prime = prime[rand_element1]
        self.base = primes[rand_element2]

    def start(self):
        """Start communication client to listen for incoming connections
        :return: None
        """
        self.socket = socket()
        self.socket.connect((self.host, self.port))
        time.sleep(2)
        self.socket.close()
        # self.__client_key_exchange()
