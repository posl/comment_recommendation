def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n = int(raw_input())
a = map(int, raw_input().split())

if __name__ == '__main__':
    gcd()