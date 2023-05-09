def main():
    L = int(input())
    if L == 2:
        print(2, 1)
        print(1, 2, 1)
        return
    N = 2
    M = 2
    ans = [[1, 2, 1]]
    while N * (N - 1) // 2 < L:
        ans.append([N, N + 1, 0])
        M += 1
        N += 1
    if N * (N - 1) // 2 == L:
        print(N, M)
        for x, y, z in ans:
            print(x, y, z)
        return
    ans.append([N, N + 1, N * (N - 1) // 2 - L])
    M += 1
    print(N + 1, M)
    for x, y, z in ans:
        print(x, y, z)
main()

if __name__ == '__main__':
    main()