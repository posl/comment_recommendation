def main():
    N, D = map(int, input().split())
    walls = []
    for i in range(N):
        L, R = map(int, input().split())
        walls.append([L, R])
    walls.sort()
    ans = 0
    idx = 0
    while idx < N:
        ans += 1
        for i in range(idx, N):
            if walls[i][0] <= walls[idx][0] + D - 1:
                idx += 1
            else:
                break
    print(ans)

if __name__ == '__main__':
    main()