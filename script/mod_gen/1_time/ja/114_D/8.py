def main():
    N = int(input())
    if N == 1:
        print(0)
    else:
        from math import factorial
        N_factorial = factorial(N)
        #print(N_factorial)
        divisor = []
        for i in range(1, N_factorial):
            if N_factorial % i == 0:
                divisor.append(i)
        #print(divisor)
        divisor_count = len(divisor)
        #print(divisor_count)
        divisor_count_75 = 0
        for i in range(1, divisor_count):
            if divisor_count % i == 0:
                divisor_count_75 += 1
        print(divisor_count_75)
main()

if __name__ == '__main__':
    main()