def main():
    v, a, b, c = map(int, input().split())
    while v > 0:
        if v - a <= 0:
            print("T")
            break
        if v - b <= 0:
            print("F")
            break
        if v - c <= 0:
            print("M")
            break
