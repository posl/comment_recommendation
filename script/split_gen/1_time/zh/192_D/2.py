def base_n_to_10(X, n):
    # base n to base 10
    ans = 0
    for i in range(len(X)):
        ans += int(X[-(i+1)]) * n**i
    return ans
