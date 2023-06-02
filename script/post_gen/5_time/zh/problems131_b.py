Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,L = map(int,input().split())
    k = L
    for i in range(1,N+1):
        k += i-1
    if k > 0:
        print(k)
    else:
        print(k+N-1)

=======
Suggestion 2

def get_min_diff(N, L):
    #N = len(L)
    L.sort()
    #print L
    if N%2 == 0:
        return sum(L[N/2:]) - sum(L[:N/2])
    else:
        return sum(L[N/2+1:]) - sum(L[:N/2+1])

=======
Suggestion 3

def main():
    #读取数据
    n, l = map(int, input().split())
    #计算最佳选择
    if l > 0:
        print(sum(range(l+1, l+n)))
    elif l+n-1 < 0:
        print(sum(range(l, l+n-1, -1)))
    else:
        print(sum(range(l, l+n)))

=======
Suggestion 4

def main():
    N, L = map(int, input().split())
    if L > 0:
        ans = sum([L + i - 1 for i in range(1, N)])
    elif L + N - 1 < 0:
        ans = sum([L + i - 1 for i in range(1, N)])
    else:
        ans = sum([L + i - 1 for i in range(2, N + 1)])
    print(ans)

=======
Suggestion 5

def main():
    n,l = map(int, input().split())
    res = 0
    if l >= 0:
        res = sum(range(l + 1, l + n))
    elif l + n - 1 < 0:
        res = sum(range(l, l + n - 1))
    else:
        res = sum(range(l, 0)) + sum(range(1, l + n))
    print(res)

=======
Suggestion 6

def main():
    n,l=map(int,input().split())
    if l>0:
        print(sum(range(l+1,l+n)))
    elif l+n-1<0:
        print(sum(range(l+n-1,l-1)))
    else:
        print(sum(range(l,l+n)))

=======
Suggestion 7

def solve(n, l):
    ans = 0
    for i in range(n):
        ans += l + i
    return ans - l

=======
Suggestion 8

def main():
    n, l = map(int, input().split())
    if l >= 0:
        ans = sum(range(l+1, l+n))
    elif l+n-1 <= 0:
        ans = sum(range(l, l+n-1))
    else:
        ans = sum(range(l+1, 0)) + sum(range(1, l+n))
    print(ans)

=======
Suggestion 9

def main():
    n, l = map(int, input().split())
    print(sum(range(l + 1, l + n)) if l >= 0 else sum(range(l + n, l + 1)))

=======
Suggestion 10

def main():
    n,l = map(int,input().split())
    if n==2:
        print(l+1)
    elif l>=0:
        print(sum(range(l+1,l+n)))
    elif l+n-1<0:
        print(sum(range(l+n-1,l-1,-1)))
    else:
        print(sum(range(l,l+n-1)))
