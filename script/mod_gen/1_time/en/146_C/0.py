def main():
    a, b, x = map(int, input().split())
    if x < a:
        print(0)
        return
    x -= a
    if x < b:
        print(0)
        return
    x -= b
    if x < b:
        print(0)
        return
    x //= b
    if x < 9:
        print(1)
        return
    x //= 9
    if x < 9:
        print(10)
        return
    x //= 9
    if x < 9:
        print(100)
        return
    x //= 9
    if x < 9:
        print(1000)
        return
    x //= 9
    if x < 9:
        print(10000)
        return
    x //= 9
    if x < 9:
        print(100000)
        return
    x //= 9
    if x < 9:
        print(1000000)
        return
    x //= 9
    if x < 9:
        print(10000000)
        return
    x //= 9
    if x < 9:
        print(100000000)
        return
    x //= 9
    if x < 9:
        print(1000000000)
        return
    x //= 9
    print(1000000000 + x)
main()
