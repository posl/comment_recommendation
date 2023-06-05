def solve(n):
    ans = 0
    for i in range(1, 10):
        for j in range(10):
            if i == j:
                continue
            for k in range(1, 20):
                num = 0
                for l in range(k):
                    num = num * 10 + i
                for l in range(k):
                    num = num * 10 + j
                if num <= n:
                    ans += 1
    return ans

if __name__ == '__main__':
    solve()