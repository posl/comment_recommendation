def main():
    L = int(input())
    N = 2
    M = 0
    ans = []
    for i in range(20):
        if L & (1 << i):
            ans.append([i + 1, i + 2, 0])
            ans.append([i + 1, i + 2, 1 << i])
            N += 1
            M += 2
    for i in range(20):
        if L & (1 << i):
            continue
        ans.append([i + 1, 20, 0])
        N += 1
        M += 1
    print(N, M)
    for i in range(M):
        print(*ans[i])

if __name__ == '__main__':
    main()