def main():
    N = int(input())
    W = list(map(int, input().split()))
    min = 100000000000
    for i in range(1, N):
        S1 = sum(W[:i])
        S2 = sum(W[i:])
        if abs(S1 - S2) < min:
            min = abs(S1 - S2)
    print(min)

if __name__ == '__main__':
    main()