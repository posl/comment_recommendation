def main():
    a, b, w = map(int, input().split())
    w *= 1000
    # a <= x <= b
    # a*x <= w <= b*x
    # x <= w/a <= x <= w/b
    min_x = w // b
    max_x = w // a
    if min_x * a <= w <= max_x * b:
        print(min_x, max_x)
    else:
        print("UNSATISFIABLE")
main()
