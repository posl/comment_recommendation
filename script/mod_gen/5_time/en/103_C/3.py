def f(m):
    return sum(m % a for a in A)
N = int(input())
A = list(map(int, input().split()))
l = 0
r = 10**9+1
while r - l > 1:
    m = (r + l) // 2
    if f(m) < f(m+1):
        r = m
    else:
        l = m
print(f(r))

if __name__ == '__main__':
    f()