def solve():
    n = int(input())
    n_str = str(n)
    n_len = len(n_str)
    ans = 0
    for i in range(n_len):
        for j in range(i+1, n_len):
            x = int(n_str[:i+1])
            y = int(n_str[i+1:j+1])
            ans = max(ans, x*y)
    print(ans)
