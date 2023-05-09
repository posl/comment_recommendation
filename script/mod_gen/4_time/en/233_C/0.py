def main():
    N, X = map(int, input().split())
    L = []
    A = []
    for _ in range(N):
        l = list(map(int, input().split()))
        L.append(l[0])
        A.append(l[1:])
    ans = 0
    for i in range(2**N):
        tmp = 1
        for j in range(N):
            if (i >> j) & 1:
                tmp *= A[j][0]
            else:
                tmp *= A[j][-1]
        if tmp <= X:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()