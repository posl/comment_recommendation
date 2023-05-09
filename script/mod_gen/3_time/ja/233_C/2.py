def main():
    N, X = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    ans = 0
    for i in range(2 ** N):
        tmp = 1
        for j in range(N):
            if ((i >> j) & 1):
                tmp *= A[j][1 + (i >> j) % A[j][0]]
        if tmp <= X:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()