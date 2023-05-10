def solve(n):
    if n == 0:
        return "0"
    ans = ""
    while n:
        if n % 2:
            ans = "1" + ans
        else:
            ans = "0" + ans
        n = (n - (n % 2)) // -2
    return ans
