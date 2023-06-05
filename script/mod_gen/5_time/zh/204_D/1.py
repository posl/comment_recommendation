def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    t1 = 0
    t2 = 0
    for i in range(N):
        if t1 <= t2:
            t1 += T[N - 1 - i]
        else:
            t2 += T[N - 1 - i]
    print(max(t1, t2))

if __name__ == '__main__':
    main()