def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    a.reverse()
    b.reverse()
    left = 0
    right = 10**10
    while right - left > 10**-5:
        mid = (left + right) / 2
        if check(n, a, b, mid):
            right = mid
        else:
            left = mid
    print(right)
