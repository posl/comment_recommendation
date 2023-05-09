def main():
    import math
    K = int(input())
    N = 1
    while True:
        if math.factorial(N) % K == 0:
            print(N)
            exit()
        N += 1

if __name__ == '__main__':
    main()