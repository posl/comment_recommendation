Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

n,x=map(int,raw_input().split())
a=map(int,raw_input().split())
a.sort()
ans=abs(x-a[0])
for i in range(1,n):
    ans=gcd(ans,abs(x-a[i]))
print ans

=======
Suggestion 2

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

n,x=map(int,input().split())
a=list(map(int,input().split()))
a.append(x)
a.sort()
b=[a[i+1]-a[i] for i in range(n)]
ans=b[0]
for i in range(1,n):
    ans=gcd(ans,b[i])
print(ans)

=======
Suggestion 3

def main():
    n,x = map(int,input().split())
    x_list = list(map(int,input().split()))
    x_list.append(x)
    x_list.sort()
    x_list = [x_list[i+1]-x_list[i] for i in range(n)]
    import math
    def gcd(a,b):
        if b == 0:
            return a
        else:
            return gcd(b,a%b)
    answer = x_list[0]
    for i in range(1,n):
        answer = gcd(answer,x_list[i])
    print(answer)

=======
Suggestion 4

def solve(n, x, xs):
    xs.sort()
    ds = []
    for i in range(n-1):
        ds.append(xs[i+1] - xs[i])
    ds.sort()
    if n == 1:
        return ds[0]
    else:
        return gcd(ds[0], ds[1])

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    if n == 1:
        print(x_list[1] - x_list[0])
    else:
        x_list_diff = [x_list[i+1] - x_list[i] for i in range(n)]
        x_list_diff.sort()
        print(x_list_diff[0])

=======
Suggestion 6

def main():
    n,x = map(int,input().split())
    x_list = list(map(int,input().split()))
    x_list.append(x)
    x_list.sort()
    d_list = []
    for i in range(n):
        d_list.append(x_list[i+1] - x_list[i])
    d = d_list[0]
    for i in range(1,n):
        d = gcd(d,d_list[i])
    print(d)

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    d_list = []
    for i in range(n):
        d_list.append(x_list[i+1] - x_list[i])
    d_list.sort()
    d = d_list[0]
    for i in range(n):
        d = gcd(d, d_list[i])
    print(d)

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = [x[i + 1] - x[i] for i in range(N)]
    import math
    ans = math.gcd(*d)
    print(ans)

=======
Suggestion 9

def main():
    n,x = map(int,input().split())
    x_list = list(map(int,input().split()))
    x_list.sort()
    if n == 1:
        print(abs(x_list[0]-x))
    else:
        x_list.append(x)
        x_list.sort()
        x_list2 = []
        for i in range(n+1):
            x_list2.append(abs(x_list[i+1]-x_list[i]))
        print(gcd_list(x_list2))

=======
Suggestion 10

def main():
    N, X = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(X)
    x_list.sort()
    d_list = []
    for i in range(N):
        d_list.append(x_list[i + 1] - x_list[i])
    gcd = d_list[0]
    for i in range(N - 1):
        gcd = calc_gcd(gcd, d_list[i + 1])
    print(gcd)
