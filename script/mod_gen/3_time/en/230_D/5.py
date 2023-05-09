def main():
    N, D = map(int, input().split())
    walls = []
    for i in range(N):
        L, R = map(int, input().split())
        walls.append([L, R])
    walls.sort(key=lambda x: x[1])
    #print(walls)
    ans = 0
    i = 0
    while i < N:
        ans += 1
        j = i + 1
        while j < N and walls[j][0] <= walls[i][1] + D:
            j += 1
        i = j
    print(ans)

if __name__ == '__main__':
    main()