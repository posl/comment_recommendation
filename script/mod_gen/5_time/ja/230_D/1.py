def main():
    N, D = map(int, input().split())
    Ls = []
    Rs = []
    for i in range(N):
        L, R = map(int, input().split())
        Ls.append(L)
        Rs.append(R)
    Ls.sort()
    Rs.sort()
    ans = 0
    for i in range(N):
        ans += 1
        if Rs[i] - Ls[i] >= D:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()