def allowance(a, b, c):
    return max(a * 10 + b + c, a + b * 10 + c, a + b + c * 10)

if __name__ == '__main__':
    allowance()