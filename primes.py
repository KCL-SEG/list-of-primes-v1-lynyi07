"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(num): 
    for i in range(2, num):
        if (num%i==0): 
            return False
    return True

def primes(number_of_primes):
    list = []
    i = 2
    while len(list) < number_of_primes: 
        if isPrime(i): 
            list.append(i); 
        i= i + 1
    return list
