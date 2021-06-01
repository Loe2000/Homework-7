def fizzBuzz(a) :
    if (a % 15 == 0):
        return "FizzBuzz"
    if ( a % 3 == 0 ):
        return "Fizz"
    if ( a % 5 == 0 ):
        return "Buzz"
    return a

def main() :
    for i in range(100):
        print(fizzBuzz(i + 1))

main()
