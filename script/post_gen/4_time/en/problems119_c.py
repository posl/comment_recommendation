Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(i, a, b, c):
    if i == N:
        if min(a, b, c) > 0:
            return abs(a - A) + abs(b - B) + abs(c - C) - 30
        else:
            return float('inf')
    res0 = dfs(i + 1, a, b, c)
    res1 = dfs(i + 1, a + L[i], b, c) + 10
    res2 = dfs(i + 1, a, b + L[i], c) + 10
    res3 = dfs(i + 1, a, b, c + L[i]) + 10
    return min(res0, res1, res2, res3)

N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
print(dfs(0, 0, 0, 0))

=======
Suggestion 2

def dfs(i, a, b, c):
    if i == N:
        return abs(a-A) + abs(b-B) + abs(c-C) - 30 if min(a, b, c) > 0 else 10**9
    ret0 = dfs(i+1, a, b, c)
    ret1 = dfs(i+1, a+l[i], b, c) + 10 if a else 10**9
    ret2 = dfs(i+1, a, b+l[i], c) + 10 if b else 10**9
    ret3 = dfs(i+1, a, b, c+l[i]) + 10 if c else 10**9
    return min(ret0, ret1, ret2, ret3)

N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]
print(dfs(0, 0, 0, 0))

=======
Suggestion 3

def f(i, a, b, c):
    if i == N:
        return abs(a - A) + abs(b - B) + abs(c - C) - 30 if min(a, b, c) > 0 else 10 ** 9
    ret0 = f(i + 1, a, b, c)
    ret1 = f(i + 1, a + l[i], b, c) + 10 if a else 10 ** 9
    ret2 = f(i + 1, a, b + l[i], c) + 10 if b else 10 ** 9
    ret3 = f(i + 1, a, b, c + l[i]) + 10 if c else 10 ** 9
    return min(ret0, ret1, ret2, ret3)

N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]
print(f(0, 0, 0, 0))

=======
Suggestion 4

def dfs(cur, a, b, c):
    if cur == N:
        return abs(a-A) + abs(b-B) + abs(c-C) - 30 if min(a, b, c) > 0 else 10**9
    ret0 = dfs(cur+1, a, b, c)
    ret1 = dfs(cur+1, a+L[cur], b, c) + 10
    ret2 = dfs(cur+1, a, b+L[cur], c) + 10
    ret3 = dfs(cur+1, a, b, c+L[cur]) + 10
    return min(ret0, ret1, ret2, ret3)

N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
print(dfs(0, 0, 0, 0))

=======
Suggestion 5

def dfs(i, a, b, c):
    if i == N:
        return abs(a-A) + abs(b-B) + abs(c-C) - 30 if min(a, b, c) > 0 else 10**10
    ret0 = dfs(i+1, a, b, c)
    ret1 = dfs(i+1, a+l[i], b, c) + 10 if a > 0 else 10**10
    ret2 = dfs(i+1, a, b+l[i], c) + 10 if b > 0 else 10**10
    ret3 = dfs(i+1, a, b, c+l[i]) + 10 if c > 0 else 10**10
    ret4 = dfs(i+1, a, b, c) + (0 if l[i] == 1 else 1)
    ret5 = dfs(i+1, a, b, c) + (0 if l[i] == 2 else 1)
    return min(ret0, ret1, ret2, ret3, ret4, ret5)

N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]
print(dfs(0, 0, 0, 0))

=======
Suggestion 6

def main():
    N, A, B, C = map(int, input().split())
    L = [int(input()) for i in range(N)]
    print(dfs(0, 0, 0, 0))

=======
Suggestion 7

def main():
    N, A, B, C = map(int, input().split())
    L = [int(input()) for _ in range(N)]
    INF = 10 ** 9

    def dfs(cur, a, b, c):
        if cur == N:
            return abs(a-A) + abs(b-B) + abs(c-C) - 30 if min(a, b, c) > 0 else INF
        ret0 = dfs(cur+1, a, b, c)
        ret1 = dfs(cur+1, a+L[cur], b, c) + 10
        ret2 = dfs(cur+1, a, b+L[cur], c) + 10
        ret3 = dfs(cur+1, a, b, c+L[cur]) + 10
        return min(ret0, ret1, ret2, ret3)

    print(dfs(0, 0, 0, 0))

=======
Suggestion 8

def main():
    N, A, B, C = map(int, input().split())
    L = [int(input()) for _ in range(N)]
    ans = 10 ** 9
    for i in range(4 ** N):
        a, b, c = 0, 0, 0
        cost = 0
        for j in range(N):
            if (i >> (2 * j)) & 3 == 1:
                if a == 0:
                    a = L[j]
                else:
                    a += L[j]
                cost += 10
            elif (i >> (2 * j)) & 3 == 2:
                if b == 0:
                    b = L[j]
                else:
                    b += L[j]
                cost += 10
            elif (i >> (2 * j)) & 3 == 3:
                if c == 0:
                    c = L[j]
                else:
                    c += L[j]
                cost += 10
        if a == 0 or b == 0 or c == 0:
            continue
        cost += abs(A - a) + abs(B - b) + abs(C - c) - 30
        ans = min(ans, cost)
    print(ans)

=======
Suggestion 9

def solve():
    N,A,B,C = map(int,input().split())
    L = [int(input()) for _ in range(N)]
    ans = 10**9
    for i in range(4**N):
        a = b = c = 0
        cost = 0
        for j in range(N):
            if (i >> j*2) & 3 == 1:
                if a == 0:
                    a = L[j]
                else:
                    a += L[j]
                cost += 10
            elif (i >> j*2) & 3 == 2:
                if b == 0:
                    b = L[j]
                else:
                    b += L[j]
                cost += 10
            elif (i >> j*2) & 3 == 3:
                if c == 0:
                    c = L[j]
                else:
                    c += L[j]
                cost += 10
        if a!=0 and b!=0 and c!=0:
            cost += abs(a-A) + abs(b-B) + abs(c-C) - 30
            ans = min(ans,cost)
    print(ans)

=======
Suggestion 10

def dfs ( i , a , b , c ): if i == N : # すべての竹を調べ終わったら、最小値を更新する if min ( a , b , c ) > 0 : return abs ( a - A ) + abs ( b - B ) + abs ( c - C ) - 30 # すべての竹を調べ終わったが、a, b, c のどれかが0の場合は、不可能なので、無限大を返す return INF res = INF # 竹iを使わない場合 res = min ( res , dfs ( i + 1 , a , b , c )) # 竹iをAに使う場合 res = min ( res , dfs ( i + 1 , a + L [ i ], b , c ) + 10 ) # 竹iをBに使う場合 res = min ( res , dfs ( i + 1 , a , b + L [ i ], c ) + 10 ) # 竹iをCに使う場合 res = min ( res , dfs ( i + 1 , a , b , c + L [ i ]) + 10 ) return res

N , A , B , C = map ( int , input (). split ()) L = [ int ( input ()) for _ in range ( N )] INF = float ( "inf" ) print ( dfs ( 0 , 0 , 0 , 0 ))
