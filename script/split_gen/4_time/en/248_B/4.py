def solve(a, b, k):
    cnt = 0
    while a < b:
        a = a * k
        cnt = cnt + 1
    return cnt
