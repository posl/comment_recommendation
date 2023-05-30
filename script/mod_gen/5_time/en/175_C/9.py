def solve():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x/d > k:
        return x - d*k
    else:
        k -= x//d
        x = x%d
        if k%2 == 0:
            return x
        else:
            return d-x
print(solve())
