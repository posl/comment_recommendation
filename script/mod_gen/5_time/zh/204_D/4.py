def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort(reverse=True)
    T1 = 0
    T2 = 0
    for i in range(N):
        if T1 < T2:
            T1 += T[i]
        else:
            T2 += T[i]
    print(max(T1, T2))

if __name__ == '__main__':
    main()