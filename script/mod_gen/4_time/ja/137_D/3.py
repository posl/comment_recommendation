def main():
    N, M = map(int, input().split())
    work = []
    for _ in range(N):
        A, B = map(int, input().split())
        work.append((A, B))
    work.sort()
    ans = 0
    for i in range(N):
        if work[i][0] > M:
            break
        ans += work[i][1]
        M -= work[i][0]
    print(ans)
main()

if __name__ == '__main__':
    main()