def main():
    N, C = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(N)]
    ABC.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        ans += ABC[i][2]
        for j in range(i+1, N):
            if ABC[i][1] < ABC[j][0]:
                ans += C * (ABC[j][0] - ABC[i][1])
                break
    print(ans)

if __name__ == '__main__':
    main()