def solve():
    N = int(input())
    dic = {}
    for i in range(N):
        s = input()
        s = ''.join(sorted(s))
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
    ans = 0
    for k in dic:
        ans += dic[k] * (dic[k] - 1) // 2
    print(ans)

if __name__ == '__main__':
    solve()