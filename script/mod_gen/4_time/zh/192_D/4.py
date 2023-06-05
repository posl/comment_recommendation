def base_n(n, x):
    ans = 0
    for i in range(len(x)):
        ans = ans * n + int(x[i])
    return ans

if __name__ == '__main__':
    base_n()