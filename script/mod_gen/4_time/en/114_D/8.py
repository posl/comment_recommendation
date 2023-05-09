def main():
    n = int(input())
    #print(n)
    #print("n =", n)
    #print("n! =", factorial(n))
    result = 0
    for i in range(1, factorial(n) + 1):
        if factorial(n) % i == 0:
            #print("i =", i)
            #print("i! =", factorial(i))
            if len(divisors(factorial(i))) == 75:
                result += 1
    print(result)

if __name__ == '__main__':
    main()