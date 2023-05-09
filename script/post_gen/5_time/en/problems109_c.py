Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = []
    for i in range(N):
        d.append(x[i+1]-x[i])
    ans = d[0]
    for i in range(1,N):
        ans = gcd(ans,d[i])
    print(ans)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = []
    for i in range(N):
        d.append(x[i+1] - x[i])
    print(gcd(d))

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    d_list = []
    for i in range(n):
        d_list.append(x_list[i+1] - x_list[i])
    d = d_list[0]
    for i in range(n-1):
        d = gcd(d, d_list[i+1])
    print(d)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = []
    for i in range(N):
        d.append(abs(x[i+1] - x[i]))
    ans = d[0]
    for i in range(1, N):
        ans = gcd(ans, d[i])
    print(ans)

=======
Suggestion 5

def solve():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = [x[i+1] - x[i] for i in range(N)]
    import functools
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    print(functools.reduce(gcd, d))

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    d_list = [x_list[i+1] - x_list[i] for i in range(n)]
    d = d_list[0]
    for i in range(1, n):
        d = gcd(d, d_list[i])
    print(d)

=======
Suggestion 7

def main():
    n,x = map(int,input().split())
    x_list = list(map(int,input().split()))
    x_list.append(x)
    x_list.sort()
    diff_list = []
    for i in range(n):
        diff_list.append(x_list[i+1]-x_list[i])
    import math
    ans = math.gcd(diff_list[0],diff_list[1])
    for i in range(2,n):
        ans = math.gcd(ans,diff_list[i])
    print(ans)

=======
Suggestion 8

def main():
    n,x = map(int,input().split())
    cities = list(map(int,input().split()))
    cities.append(x)
    cities.sort()
    diff = []
    for i in range(1,n+1):
        diff.append(cities[i]-cities[i-1])
    gcd = diff[0]
    for i in range(1,n):
        gcd = euclid(gcd,diff[i])
    print(gcd)

=======
Suggestion 9

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

n,x = map(int,input().split())
x_i = list(map(int,input().split()))

d = abs(x-x_i[0])
for i in range(1,n):
    d = gcd(d,abs(x-x_i[i]))

print(d)

=======
Suggestion 10

def calc_distance(x, y):
    return abs(x - y)
