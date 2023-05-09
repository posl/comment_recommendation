def main():
    a, b, w = map(int, input().split())
    w *= 1000
    min_orange = w // b
    max_orange = w // a
    if min_orange * a <= w <= max_orange * b:
        print(min_orange, max_orange)
    else:
        print("UNSATISFIABLE")
