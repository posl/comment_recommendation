def solve(n):
    ans = 0
    for i in range(1, int(n**0.25)+1):
        if n%i == 0:
            m = n//i
            for j in range(1, int(m**0.25)+1):
                if m%j == 0:
                    k = m//j
                    if k%2 == 1 and k != 1:
                        ans += 1
    return ans

if __name__ == '__main__':
    solve()