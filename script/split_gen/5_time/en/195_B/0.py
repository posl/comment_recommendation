def main():
    a, b, w = map(int, input().split())
    w *= 1000
    if w % a == 0:
        min = w // a
    else:
        min = w // a + 1
    max = w // b
    if min > max:
        print("UNSATISFIABLE")
    else:
        print(min, max)
