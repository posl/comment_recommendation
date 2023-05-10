def solve(n):
    result = ""
    while n > 0:
        if n % 2 == 0:
            n = n // 2
            result = "B" + result
        else:
            n = n - 1
            result = "A" + result
    return result
n = int(input())
print(solve(n))

if __name__ == '__main__':
    solve()