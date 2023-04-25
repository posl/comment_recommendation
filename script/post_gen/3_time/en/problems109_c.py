Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

N, X = map(int, input().split())
x = list(map(int, input().split()))
x.append(X)
x.sort()
x = [x[i+1] - x[i] for i in range(N)]
ans = x[0]
for i in range(1, N):
    ans = gcd(ans, x[i])
print(ans)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    D = x[1] - x[0]
    for i in range(1, N):
        D = gcd(D, x[i + 1] - x[i])
    print(D)

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    diff_list = []
    for i in range(len(x_list)-1):
        diff_list.append(x_list[i+1]-x_list[i])
    diff_list.sort()
    if len(diff_list) == 1:
        print(diff_list[0])
    else:
        gcd = diff_list[0]
        for i in range(1, len(diff_list)):
            gcd = euclid(gcd, diff_list[i])
        print(gcd)

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    if n == 1:
        print(x_list[1] - x_list[0])
    else:
        d_list = []
        for i in range(n):
            d_list.append(x_list[i+1] - x_list[i])
        import math
        d = math.gcd(d_list[0], d_list[1])
        for i in range(n-2):
            d = math.gcd(d, d_list[i+2])
        print(d)

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    cities = list(map(int, input().split()))
    cities.append(x)
    cities.sort()

    distances = []
    for i in range(n):
        distances.append(cities[i+1] - cities[i])

    gcd = distances[0]
    for i in range(n-1):
        gcd = calc_gcd(gcd, distances[i+1])

    print(gcd)

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(X)
    x_list.sort()
    x_diff_list = [x_list[i+1] - x_list[i] for i in range(N)]
    gcd = x_diff_list[0]
    for i in range(1, N):
        gcd = gcd_calc(gcd, x_diff_list[i])
    print(gcd)

=======
Suggestion 7

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

n, x = map(int, input().split())
nums = list(map(int, input().split()))

nums.append(x)
nums.sort()
diff = [nums[i+1] - nums[i] for i in range(n)]
ans = diff[0]
for i in range(1, n):
    ans = gcd(ans, diff[i])

print(ans)

=======
Suggestion 8

def find_gcd(a,b):
    if b == 0:
        return a
    else:
        return find_gcd(b,a%b)

n,x = map(int,input().split())
x_list = list(map(int,input().split()))
x_list.append(x)
x_list.sort()
diff_list = []
for i in range(n):
    diff_list.append(x_list[i+1]-x_list[i])
gcd = diff_list[0]
for i in range(n-1):
    gcd = find_gcd(gcd,diff_list[i+1])
print(gcd)

=======
Suggestion 9

def get_input():
    n,x = map(int,input().split())
    x_list = list(map(int,input().split()))
    return (n,x,x_list)
