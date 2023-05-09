def main():
    a, b, c, k = map(int, input().split())
    if k <= a:
        print(k)
        return
    if k <= a + b:
        print(a)
        return
    print(a - (k - a - b))
