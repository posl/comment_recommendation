Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    uf = UnionFind(n)
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            uf.union(a - 1, b - 1)
        elif t == 2:
            if uf.same(a - 1, b - 1):
                uf.union(a - 1, b - 1)
                uf.union(b - 1, a - 1)
        else:
            if uf.same(a - 1, b - 1):
                print("Yes")
            else:
                print("No")

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    follow = [[0] * N for _ in range(N)]
    for _ in range(Q):
        t, a, b = map(int, input().split())
        a -= 1
        b -= 1
        if t == 1:
            follow[a][b] = 1
        elif t == 2:
            follow[b][a] = 1
        else:
            if follow[a][b]:
                print('Yes')
            elif any(follow[a][c] and follow[c][b] for c in range(N)):
                print('Yes')
            else:
                print('No')

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    follow = [[0] * N for _ in range(N)]
    for _ in range(Q):
        t, a, b = map(int, input().split())
        a -= 1
        b -= 1
        if t == 1:
            follow[a][b] = 1
        elif t == 2:
            follow[b][a] = 1
        else:
            if follow[a][b] == 1:
                print('Yes')
            else:
                print('No')

=======
Suggestion 4

def main():
    n, q = map(int, input().split())
    follow = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow[a][b] = 1
        elif t == 2:
            follow[b][a] = 1
        else:
            ans = 'No'
            for i in range(1, n + 1):
                if follow[a][i] and follow[i][b]:
                    ans = 'Yes'
                    break
            print(ans)

=======
Suggestion 5

def main():
    # input
    N, Q = map(int, input().split())
    Ts = [[0]*3 for _ in range(Q)]
    for i in range(Q):
        Ts[i] = list(map(int, input().split()))

    # compute
    follow = [[False]*(N+1) for _ in range(N+1)]
    for i in range(Q):
        if Ts[i][0] == 1:
            follow[Ts[i][1]][Ts[i][2]] = True
        elif Ts[i][0] == 2:
            follow[Ts[i][1]][Ts[i][2]] = False
        else:
            ans = 'No'
            for j in range(1, N+1):
                if follow[Ts[i][1]][j] and follow[j][Ts[i][2]]:
                    ans = 'Yes'
                    break
            print(ans)

    # output

=======
Suggestion 6

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

=======
Suggestion 7

def main():
    N,Q = map(int,input().split())
    follow = [set() for _ in range(N)]
    for _ in range(Q):
        t,a,b = map(int,input().split())
        if t == 1:
            follow[a-1].add(b-1)
        elif t == 2:
            follow[b-1].add(a-1)
        else:
            if a-1 in follow[b-1]:
                print('Yes')
            else:
                print('No')

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    f = [set() for i in range(N)]
    for i in range(Q):
        t, a, b = map(lambda x: int(x) - 1, input().split())
        if t == 0:
            f[a].add(b)
            f[b].add(a)
        elif t == 1:
            f[a].discard(b)
            f[b].discard(a)
        else:
            print('Yes' if f[a] & f[b] else 'No')

main()

=======
Suggestion 9

def main():
    n, q = map(int, input().split())

    # 各ユーザーのフォローしているユーザーのリスト
    followed_by = [[] for _ in range(n)]
    # 各ユーザーのフォローされているユーザーのリスト
    following = [[] for _ in range(n)]

    for _ in range(q):
        t, a, b = map(int, input().split())
        a -= 1
        b -= 1

        if t == 1:
            followed_by[a].append(b)
            following[b].append(a)
        elif t == 2:
            if b in followed_by[a]:
                followed_by[a].remove(b)
                following[b].remove(a)
        else:
            if any(f in followed_by[a] for f in following[b]):
                print("Yes")
            else:
                print("No")

=======
Suggestion 10

def get_input():
    N,Q = map(int, input().split())
    return N,Q
