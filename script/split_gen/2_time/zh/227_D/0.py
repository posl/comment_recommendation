def solve():
    n = int(input())
    count = 0
    for a in range(1, n+1):
        for b in range(a, n+1):
            if a * b > n:
                break
            for c in range(b, n+1):
                if a * b * c > n:
                    break
                count += 1
    print(count)
solve()
