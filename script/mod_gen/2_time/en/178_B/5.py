def maxProduct(a, b, c, d):
    if a <= 0 and b >= 0 and c <= 0 and d >= 0:
        return max(abs(a) * abs(c), abs(a) * abs(d), abs(b) * abs(c), abs(b) * abs(d))
    else:
        return max(a * c, a * d, b * c, b * d)
a, b, c, d = map(int, input().split())
print(maxProduct(a, b, c, d))

if __name__ == '__main__':
    maxProduct()