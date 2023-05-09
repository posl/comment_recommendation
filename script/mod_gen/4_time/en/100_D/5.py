def main():
    N, M = map(int, input().split())
    xyz = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(8):
        xyz.sort(reverse=True, key=lambda x:sum([x[i] for i in range(3)]))
        tmp = 0
        for j in range(M):
            tmp += sum([xyz[j][i] for i in range(3)])
        ans = max(ans, abs(tmp))
    print(ans)

if __name__ == '__main__':
    main()