Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    ans = 10**9
    for i in range(n-k+1):
        if x[i] <= 0 <= x[i+k-1]:
            ans = min(ans, min(abs(x[i]),abs(x[i+k-1]))*2 + max(abs(x[i]),abs(x[i+k-1])))
        elif x[i] < 0:
            ans = min(ans, abs(x[i]) + x[i+k-1])
        else:
            ans = min(ans, x[i+k-1] + abs(x[i]))
    print(ans)

=======
Suggestion 2

def solve():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10 ** 9
    for i in range(n - k + 1):
        l = x[i]
        r = x[i + k - 1]
        if l * r <= 0:
            ans = min(ans, min(abs(l), abs(r)) + r - l)
        else:
            ans = min(ans, max(abs(l), abs(r)))
    print(ans)
solve()

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    if k == 1:
        print(0)
        exit()
    ans = 10**9
    for i in range(n-k+1):
        a = x[i]
        b = x[i+k-1]
        ans = min(ans, b-a+min(abs(a), abs(b)))
    print(ans)

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    #print(n,k,x)
    if k == 1:
        print(0)
    else:
        #x.sort()
        #print(x)
        result = 0
        for i in range(0,k-1):
            result += x[i]
        print(result)

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    ans = 10**8
    for i in range(n-k+1):
        l = x[i]
        r = x[i+k-1]
        if l*r >= 0:
            ans = min(ans,max(abs(l),abs(r)))
        else:
            ans = min(ans,r-l+min(abs(l),abs(r)))
    print(ans)

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    ans = 10**9
    for i in range(n-k+1):
        l = x[i]
        r = x[i+k-1]
        if l*r < 0:
            ans = min(ans,min(abs(l),abs(r))+r-l)
        else:
            ans = min(ans,max(abs(l),abs(r)))
    print(ans)

=======
Suggestion 8

def solve():
    n,k=map(int,input().split())
    x=list(map(int,input().split()))
    ans=float('inf')
    for i in range(n-k+1):
        left=x[i]
        right=x[i+k-1]
        if left*right<=0:
            ans=min(ans,min(-2*left+right,right-2*left))
        else:
            ans=min(ans,max(abs(left),abs(right)))
    print(ans)

=======
Suggestion 9

def solve(N, K, xs):
    #print(N,K,xs)
    if K == 1:
        return 0
    if K == N:
        return xs[-1] - xs[0]
    if K == 2:
        return min(xs[-1] - xs[0], xs[-2] - xs[0], xs[-1] - xs[1])
    if K == N - 1:
        return min(xs[-1] - xs[0], xs[-1] - xs[1], xs[-2] - xs[0])
    return min(xs[-1] - xs[0] + min(xs[-1] - xs[1], xs[-2] - xs[0]), xs[-2] - xs[0] + xs[-1] - xs[1], xs[-1] - xs[0] + xs[-1] - xs[2])
