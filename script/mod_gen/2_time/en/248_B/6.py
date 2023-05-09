def solve(a, b, k):
    if a >= b:
        return 0
    else:
        count = 0
        while a < b:
            a = a * k
            count += 1
        return count

if __name__ == '__main__':
    solve()