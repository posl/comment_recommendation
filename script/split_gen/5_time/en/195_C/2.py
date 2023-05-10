def main():
    n = int(input())
    n_str = str(n)
    n_len = len(n_str)
    ans = 0
    for i in range(n_len):
        if i % 3 == 0:
            ans += int(n_str[n_len - i - 1])
        else:
            ans += int(n_str[n_len - i - 1]) * (10 ** (i % 3))
    print(ans)
