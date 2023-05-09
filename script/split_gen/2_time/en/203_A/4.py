def main():
    # read input
    a, b, c = map(int, input().split())
    # solve problem
    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif c == a:
        print(b)
    else:
        print(0)
