def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = [-1] * N
    ans[0] = 1
    for a, b in AB:
        if ans[a-1] == 1:
            ans[b-1] = 0
        else:
            ans[b-1] = ans[a-1]
    if 0 in ans:
        print(-1)
    else:
        print(*ans, sep='\n')

if __name__ == '__main__':
    main()