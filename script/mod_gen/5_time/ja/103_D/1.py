def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    ans = 1
    b = AB[0][1]
    for i in range(1, M):
        if AB[i][0] >= b:
            ans += 1
            b = AB[i][1]
    print(ans)

if __name__ == '__main__':
    main()