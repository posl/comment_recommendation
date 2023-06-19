def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n, m = map(int, input().split())
a = list(map(int, input().split()))
# 用于记录已经找到的满足条件的数
ans = [1] * (m + 1)
# 用于记录已经找到的满足条件的数的个数
cnt = 0

if __name__ == '__main__':
    gcd()