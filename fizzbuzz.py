def main():
    for x in range(1, 101):
        if x % 15 == 0:
            print('{} : FizzBuzz '.format(x))
        elif x % 5 == 0:
            print('{} : Buzz '.format(x))
        elif x % 3 == 0:
            print('{} : Fizz '.format(x))
main() 
