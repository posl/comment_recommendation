def solve(a, b, c, d):
    for i in range(a, b+1):
        for j in range(c, d+1):
            if is_prime(i+j):
                return 'Takahashi'
    return 'Aoki'

if __name__ == '__main__':
    solve()