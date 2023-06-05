def solve(n):
    ans = 0
    for i in range(1, 10**6):
        if i * (i-1) > 2*n:
            break
        if 2*n % i == 0:
            m = 2*n // i
            if (m-i+1) % 2 == 0:
                ans += 1
    return ans*2

if __name__ == '__main__':
    solve()