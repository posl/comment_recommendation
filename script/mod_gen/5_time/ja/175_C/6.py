def get_min_abs(x, k, d):
    x = abs(x)
    if x >= k * d:
        return x - k * d
    else:
        k -= x // d
        x = x % d
        if k % 2 == 0:
            return x
        else:
            return d - x
x, k, d = map(int, input().split())
print(get_min_abs(x, k, d))

if __name__ == '__main__':
    get_min_abs()