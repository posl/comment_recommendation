def main():
    N, D = map(int, input().split())
    walls = []
    for i in range(N):
        l, r = map(int, input().split())
        walls.append((l, r))
    walls.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        l, r = walls[i]
        if l <= ans:
            ans = ans - ans % D + r
        else:
            ans = ans - ans % D + l + D - 1
    print(ans)

if __name__ == '__main__':
    main()