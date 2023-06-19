def solve(n):
    ans = []
    while n > 0:
        if n % 2 == 0:
            n = n // 2
            ans.append("B")
        else:
            n -= 1
            ans.append("A")
    return "".join(ans[::-1])
