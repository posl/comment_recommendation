def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    P = [x - 1 for x in P]
    Q = [x - 1 for x in Q]
    a = 0
    b = 0
    for i in range(N):
        a += P[i] * math.factorial(N - i - 1)
        b += Q[i] * math.factorial(N - i - 1)
    print(abs(a - b))

if __name__ == '__main__':
    main()