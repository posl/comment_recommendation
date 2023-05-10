def calc_gen_dist(n, a):
    ans = [0] * (2**n + 1)
    for i in range(n):
        ans[a[i]] = 1
    for i in range(1, 2**n):
        ans[i] += ans[i//2] + 1
    return ans

if __name__ == '__main__':
    calc_gen_dist()