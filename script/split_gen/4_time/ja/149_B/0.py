def main():
    a, b, k = map(int, input().split())
    if k >= a:
        k -= a
        a = 0
    else:
        a -= k
        k = 0
    if k >= b:
        k -= b
        b = 0
    else:
        b -= k
        k = 0
    print(a, b)
