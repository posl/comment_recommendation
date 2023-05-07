def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = AB[0][1]
    for i in range(1, N):
        ans = max(ans, AB[i][1])
    print(ans)

if __name__ == '__main__':
    main()