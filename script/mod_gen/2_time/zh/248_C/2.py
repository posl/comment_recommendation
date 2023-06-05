def solve(a,b,k):
    cnt = 0
    while a < b:
        a = a * k
        cnt += 1
    return cnt

if __name__ == '__main__':
    solve()