def solve(a,n):
    if n == 1:
        return 0
    if n < a:
        return -1
    if n == a:
        return 1
    if n%a == 0:
        return 1 + solve(a,n//a)
    if n%10 == 1:
        return 1 + solve(a,n//10)
    return -1
a,n = map(int, input().split())
print(solve(a,n))
