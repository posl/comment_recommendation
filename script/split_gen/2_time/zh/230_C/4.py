def solve():
    n, a, b = map(int, input().split())
    p, q, r, s = map(int, input().split())
    a -= 1
    b -= 1
    p -= 1
    q -= 1
    r -= 1
    s -= 1
    ans = [['.' for _ in range(s-r+1)] for _ in range(q-p+1)]
    for i in range(max(1-a, 1-b), min(n-a, n-b)+1):
        ans[i+a-p][i+b-r] = '#'
    for i in range(max(1-a, b-n), min(n-a, b-1)+1):
        ans[i+a-p][r+b-i] = '#'
    for i in range(q-p+1):
        print(''.join(ans[i]))
