def solve():
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    ans = []
    for i in A:
        if i != X:
            ans.append(i)
    print(*ans)

if __name__ == '__main__':
    solve()