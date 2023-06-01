Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()
    ans = 10**9
    for i in range(n-k+1):
        l = x[i]
        r = x[i+k-1]
        ans = min(ans, r-l+min(abs(l),abs(r)))
    print(ans)

=======
Suggestion 2

def main():
    N,K = map(int, input().split())
    x = list(map(int, input().split()))
    #print(N,K,x)
    if K == 1:
        print(0)
    else:
        #print(x)
        #print(x[K-1])
        #print(x[0])
        #print(x[K-1] - x[0])
        #print(x[N-1] - x[K])
        print(min(x[K-1] - x[0], x[N-1] - x[K]))

main()

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = float('inf')
    for i in range(n - k + 1):
        l = x[i]
        r = x[i + k - 1]
        if l * r <= 0:
            time = min(abs(l), abs(r)) + r - l
        else:
            time = max(abs(l), abs(r))
        ans = min(ans, time)
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10 ** 9
    for i in range(n - k + 1):
        l = x[i]
        r = x[i + k - 1]
        if l * r <= 0:
            ans = min(ans, min(-l, r) * 2 + max(-l, r))
        else:
            ans = min(ans, max(l, r))
    print(ans)

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    ans = 10**9
    for i in range(n-k+1):
        l = x[i]
        r = x[i+k-1]
        if l*r <= 0:
            ans = min(ans,min(-2*l+r,r-2*r+l))
        else:
            ans = min(ans,max(l,r))
    print(ans)

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    time = float('inf')
    for i in range(n-k+1):
        if x[i]*x[i+k-1] < 0:
            t = min(abs(x[i]),abs(x[i+k-1]))*2 + max(abs(x[i]),abs(x[i+k-1]))
        else:
            t = max(abs(x[i]),abs(x[i+k-1]))
        if t < time:
            time = t
    print(time)

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    x = list(map(int,input().split()))
    ans = 10**9
    for i in range(n-k+1):
        l = x[i]
        r = x[i+k-1]
        if l*r<0:
            ans = min(ans,min(abs(l),abs(r))+r-l)
        else:
            ans = min(ans,max(abs(l),abs(r)))
    print(ans)

=======
Suggestion 9

def solve(n,k,x):
    ans = 10**9
    for i in range(n-k+1):
        lx = x[i]
        rx = x[i+k-1]
        time = rx-lx
        if lx<0 and rx<0:
            time -= lx
        elif lx<0 and 0<=rx:
            time += min(abs(lx),rx)
        else:
            time += rx
        ans = min(ans,time)
    return ans

n,k = map(int,input().split())
x = list(map(int,input().split()))
print(solve(n,k,x))

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(n-k+1):
        left = x[i]
        right = x[i+k-1]
        ans = min(ans, min(abs(left), abs(right)) + right - left)
    print(ans)
