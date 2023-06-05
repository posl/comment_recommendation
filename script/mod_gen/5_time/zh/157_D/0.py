def solve():
    n,m,k = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(m)]
    cd = [list(map(int,input().split())) for _ in range(k)]
    ans = [0]*n
    friend = [[] for _ in range(n)]
    block = [[] for _ in range(n)]
    for a,b in ab:
        friend[a-1].append(b-1)
        friend[b-1].append(a-1)
    for c,d in cd:
        block[c-1].append(d-1)
        block[d-1].append(c-1)
    for i in range(n):
        ans[i] = len(set(friend[i])-set(block[i])-{i})
    print(*ans)

if __name__ == '__main__':
    solve()