def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    L.sort()
    L.insert(0, [0, 0])
    ans = 1
    for i in range(1, N+1):
        if L[i] != L[i-1]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()