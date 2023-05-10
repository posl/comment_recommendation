def main():
    N, D = map(int, input().split())
    walls = []
    for i in range(N):
        L, R = map(int, input().split())
        walls.append((L, R))
    walls.sort(key=lambda x: x[0])
    #print(walls)
    ans = 0
    for i in range(N):
        L, R = walls[i]
        #print(L, R)
        if L > D:
            ans += 1
        if R > D:
            ans += 1
            D = L
        else:
            D = min(D, L)
        #print(ans, D)
    if D > 0:
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()