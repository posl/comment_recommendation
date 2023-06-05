Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,x = map(int,input().split())
    bag = []
    for i in range(n):
        bag.append(list(map(int,input().split()))[1:])
    ans = 0
    for i in range(1,x+1):
        if x%i == 0:
            for j in range(n):
                if i in bag[j]:
                    break
            else:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    #print(N, X, L)
    #print(L[0][1])
    ans = 0
    for i in range(N):
        for j in range(L[i][0]):
            #print(L[i][j+1])
            if X % L[i][j+1] == 0:
                #print("yes")
                for k in range(N):
                    for l in range(L[k][0]):
                        #print(L[k][l+1])
                        if X / L[i][j+1] == L[k][l+1]:
                            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N,X = map(int,input().split())
    bag = []
    for i in range(N):
        bag.append(list(map(int,input().split()))[1:])
    #print(bag)
    #print(N,X)
    cnt = 0
    for i in range(N):
        for j in range(len(bag[i])):
            if X%bag[i][j] == 0:
                tmp = X//bag[i][j]
                for k in range(N):
                    if tmp in bag[k]:
                        cnt += 1
    print(cnt)

main()

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    l = []
    for _ in range(n):
        l.append(list(map(int, input().split()))[1:])
    ans = 0
    for i in range(1, 1 << n):
        p = 1
        for j in range(n):
            if i >> j & 1:
                p *= l[j][0]
        if p == x:
            ans += 1
    print(ans)

=======
Suggestion 5

def solve(N,X,L,A):
    import itertools
    def product(A):
        import functools
        return functools.reduce(lambda x,y:x*y,A)
    def count(A,X):
        return sum(product(a) == X for a in itertools.product(*A))
    return count(A,X)

=======
Suggestion 6

def solve():
    N, X = map(int, input().split())
    bag = []
    for i in range(N):
        bag.append(list(map(int, input().split()))[1:])

    def dfs(i, X):
        if i == N:
            return 1 if X == 1 else 0
        res = 0
        for j in range(len(bag[i])):
            if X % bag[i][j] == 0:
                res += dfs(i + 1, X // bag[i][j])
        return res

    print(dfs(0, X))

solve()

=======
Suggestion 7

def get_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n // i)
    return divisors

=======
Suggestion 8

def main():
    print('hello world')

=======
Suggestion 9

def main():
    # N, X = map(int, input().split())
    # L = []
    # for i in range(N):
    #     L.append(list(map(int, input().split())))
    N, X = 3, 200
    L = [[3, 10, 10, 10], [3, 10, 10, 10], [5, 2, 2, 2, 2]]
    # N, X = 3, 1000000000000000000
    # L = [[2, 1000000000, 1000000000], [2, 1000000000, 1000000000], [2, 1000000000, 1000000000]]
    L2 = []
    for i in range(N):
        L2.append([1])
        for j in range(1, L[i][0] + 1):
            L2[i].append(L2[i][j - 1] * L[i][j])
    print(L2)
    count = 0
    for i in range(N):
        for j in range(L[i][0]):
            if X % L2[i][j] == 0 and X // L2[i][j] <= L[i][0]:
                count += L[i][0] - X // L2[i][j]
    print(count)

=======
Suggestion 10

def solve():
    N, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    # 二分探索
    def check(x):
        cnt = 0
        for a in A:
            for ai in a:
                if ai * x >= X:
                    cnt += 1
                    break
        return cnt == N

    ok = 0
    ng = 10 ** 9 + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid

    # 二分探索終了後、ok は条件を満たす最小の値となっている。
    ans = 0
    for a in A:
        for ai in a:
            if ai * ok >= X:
                ans += 1
                break

    print(ans)
