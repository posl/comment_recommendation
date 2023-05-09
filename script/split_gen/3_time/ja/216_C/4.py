def solve(n):
    ans = []
    while n > 0:
        if n % 2 == 0:
            ans.append('B')
            n = n // 2
        else:
            ans.append('A')
            n -= 1
    return ''.join(ans[::-1])
n = int(input())
print(solve(n))
