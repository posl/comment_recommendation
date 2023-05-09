def rounding(x, k):
    for i in range(k):
        if x % (10**(i+1)) <= 5 * 10**i:
            x -= x % (10**(i+1))
        else:
            x += 10**(i+1) - x % (10**(i+1))
    return x
x, k = map(int, input().split())
print(rounding(x, k))

if __name__ == '__main__':
    rounding()