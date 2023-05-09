def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    x = 0
    y = 0
    for i in range(N):
        p = 1
        q = 1
        for j in range(i+1, N):
            if P[i] > P[j]:
                p += 1
            if Q[i] > Q[j]:
                q += 1
        x += (p - 1) * factorial(N - i - 1)
        y += (q - 1) * factorial(N - i - 1)
    print(abs(x - y))

if __name__ == '__main__':
    main()