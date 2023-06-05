def main():
    a, b, k = map(int, input().split())
    if k > a:
        b -= k - a
        a = 0
    else:
        a -= k
    if b < 0:
        b = 0
    print(a, b)
