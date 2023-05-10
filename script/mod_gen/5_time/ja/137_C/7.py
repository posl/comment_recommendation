def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 0
    dic = {}
    for s in S:
        s = ''.join(sorted(s))
        if s in dic:
            ans += dic[s]
            dic[s] += 1
        else:
            dic[s] = 1
    print(ans)

if __name__ == '__main__':
    solve()