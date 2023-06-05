def is_between(a, b, c):
    if a <= b and b <= c:
        print("是")
    else:
        print("否")
a = int(input())
is_between(-2147483648, a, 2147483647)
