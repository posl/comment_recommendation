def main():
    N = int(input())
    W = list(map(int, input().split()))
    min = 100000000
    for i in range(1, N):
        S1 = 0
        S2 = 0
        for j in range(0, i):
            S1 += W[j]
        for j in range(i, N):
            S2 += W[j]
        if abs(S1 - S2) < min:
            min = abs(S1 - S2)
    print(min)

if __name__ == '__main__':
    main()