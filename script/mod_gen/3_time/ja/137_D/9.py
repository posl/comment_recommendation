def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x:x[0])
    B = [0]
    for i in range(N):
        B.append(AB[i][1])
    B.sort(reverse=True)
    ans = 0
    for i in range(N):
        if AB[i][0] <= M:
            ans += B[AB[i][0]]
            M -= 1
    print(ans)

if __name__ == '__main__':
    main()