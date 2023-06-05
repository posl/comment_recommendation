def main():
    N = int(input())
    W = list(map(int, input().split()))
    W.sort()
    T = int(sum(W)/2)
    s1 = 0
    s2 = 0
    for i in range(N):
        if s1 + W[i] <= T:
            s1 += W[i]
        else:
            s2 += W[i]
    print(abs(s2 - s1))

if __name__ == '__main__':
    main()