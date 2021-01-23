def primes(n):
    '''
    Returns all prime numbers from 1 to n
    Parameters: n, the maximum number entred 
    Return Value: ans, a list of prime numbers
    '''
    primes = [True for i in range(n+1)] 
    x = 2
    primes[0], primes[1] = False, False 
    while (x ** 2 <= n):
        if (primes[x] == True):
            for i in range(x*2, n+1, x):
                primes[i] = False
        x += 1
    ans = []
    for i in range(n+1):
        if primes[i]:
            ans.append(i)
    return ans 

def prime_factorization(n):
    '''
    Returns the prime factorization of a number in a list
    Parameters: n, an integer 
    Return value: a list of all prime factors of n 
    '''
    prime_list = primes(n)
    factorization = []
    for p in prime_list:
        while (n%p == 0):
            factorization.append(p)
            n /= p 
    return factorization

def main(): 
    print(primes(10))
    print(prime_factorization(120))

main() 
