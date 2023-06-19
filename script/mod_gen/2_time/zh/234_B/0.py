def my_sqrt(x):
    ans = 1.0
    while abs(ans * ans - x) > 1e-10:
        ans = (ans + x / ans) / 2.0
    return ans

if __name__ == '__main__':
    my_sqrt()