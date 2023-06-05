def d(N):
    if N == 0:
        return 0
    else:
        return d(N//10)+1
A, B, X = map(int, input().split())
left = 0
right = 10**9+1
while right - left > 1:
    middle = (left + right)//2
    if A*middle + B*d(middle) <= X:
        left = middle
    else:
        right = middle
print(left)
