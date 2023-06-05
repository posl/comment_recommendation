def d(n):
    if n < 10:
        return 1
    else:
        return 1 + d(n/10)
a,b,x = map(int,input().split())
left = 0
right = 10**9 + 1
while right - left > 1:
    mid = (left + right)//2
    if a*mid + b*d(mid) <= x:
        left = mid
    else:
        right = mid
print(left)

if __name__ == '__main__':
    d()