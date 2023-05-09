def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.reverse()
    ans = [0] * N
    for a, b in AB:
        if ans[a-1] == 0 and ans[b-1] == 0:
            ans[a-1] = b
            ans[b-1] = a
        elif ans[a-1] != 0:
            ans[ans[a-1]-1] = b
            ans[b-1] = ans[a-1]
            ans[a-1] = b
        elif ans[b-1] != 0:
            ans[ans[b-1]-1] = a
            ans[a-1] = ans[b-1]
            ans[b-1] = a
    for i in range(N):
        if ans[i] == 0:
            ans[i] = i+1
    if len(set(ans)) == len(ans):
        print(*ans)
    else:
        print(-1)

if __name__ == '__main__':
    main()