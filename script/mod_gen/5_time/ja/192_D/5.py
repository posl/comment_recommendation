def convert_base(n, b):
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(str(n % b))
        n //= b
    return ''.join(digits[::-1])
X = input()
M = int(input())
d = int(max(X))

if __name__ == '__main__':
    convert_base()