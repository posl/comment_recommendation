def main():
    N, M = map(int, input().split())
    work = []
    for i in range(N):
        work.append(list(map(int, input().split())))
    work.sort(key=lambda x: x[0])
    now = 0
    ans = 0
    for i in range(N):
        if work[i][0] - now <= M:
            ans += work[i][1]
            now = work[i][0]
        else:
            ans += M * work[i][1]
            break
        if now == M:
            break
    print(ans)

if __name__ == '__main__':
    main()