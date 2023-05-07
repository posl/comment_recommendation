def solve():
    N, Q = map(int, input().split())
    follow = [set() for i in range(N+1)]
    for i in range(Q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow[a].add(b)
        elif t == 2:
            if a in follow[b]:
                print("Yes")
            else:
                print("No")
        else:
            if len(follow[a] & follow[b]) > 0:
                print("Yes")
            else:
                print("No")
solve()

if __name__ == '__main__':
    solve()