def main():
    N, M = map(int, input().split())
    cake = [list(map(int, input().split())) for i in range(N)]
    ans = 0
    for i in range(8):
        cake.sort(key=lambda x: -x[i % 3] if i >= 3 else x[i % 3])
        ans = max(ans, sum([sum(cake[i][:3]) for i in range(M)]))
    print(ans)

if __name__ == '__main__':
    main()