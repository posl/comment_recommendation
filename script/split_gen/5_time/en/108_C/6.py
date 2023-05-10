def main():
    # Take input Here and Call solution function
    n, k = get_ints_in_variables()
    ans = 0
    if k % 2 == 0:
        for i in range(1, n + 1):
            if i % k == 0:
                ans += n // k
            elif i % k == k // 2:
                ans += n // k
                if n % k >= k // 2:
                    ans += 1
    else:
        for i in range(1, n + 1):
            if i % k == 0:
                ans += n // k
    print(ans)
