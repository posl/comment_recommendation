def main():
    k = int(input())
    ans = 0
    base = 1
    while k > 0:
        ans += base * (k % 2)
        k //= 2
        base *= 10
    print(ans)
