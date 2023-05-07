def main():
    N, D = map(int, input().split())
    walls = []
    for _ in range(N):
        L, R = map(int, input().split())
        walls.append((L, R))
    walls.sort()
    ans = 0
    i = 0
    while i < N:
        j = i
        while j < N and walls[j][0] <= walls[i][1] + D:
            j += 1
        ans += 1
        i = j
    print(ans)

if __name__ == '__main__':
    main()