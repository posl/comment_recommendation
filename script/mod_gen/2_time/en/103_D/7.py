def main():
    N, M = map(int, input().split())
    L = [0] * M
    for i in range(M):
        a, b = map(int, input().split())
        L[i] = [a, b]
    L.sort()
    ans = 0
    for i in range(M):
        for j in range(i + 1, M):
            if L[i][1] <= L[j][0]:
                ans += 1
                break
    print(ans)

if __name__ == '__main__':
    main()