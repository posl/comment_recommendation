def main():
    n, l = map(int, input().split())
    ans = 0
    min_diff = 10**9
    for i in range(n):
        taste = l+i
        ans += taste
        if abs(taste) < min_diff:
            min_diff = abs(taste)
            min_taste = taste
    print(ans-min_taste)
