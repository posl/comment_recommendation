def calc_expectation(a, b, c):
    if a == 100 or b == 100 or c == 100:
        return 0
    if (a, b, c) in memo:
        return memo[(a, b, c)]
    ans = 0
    ans += calc_expectation(a+1, b, c) * a
    ans += calc_expectation(a, b+1, c) * b
    ans += calc_expectation(a, b, c+1) * c
    ans += 100
    ans /= (a+b+c)
    memo[(a, b, c)] = ans
    return ans
memo = {}
a, b, c = map(int, input().split())
print(calc_expectation(a, b, c))

if __name__ == '__main__':
    calc_expectation()