def main():
    a, b, w = map(int, input().split())
    w *= 1000
    min = w // b
    max = w // a
    if min == max:
        if w % min == 0:
            print(min, max)
        else:
            print("UNSATISFIABLE")
    else:
        if w % min == 0 and w % max == 0:
            print(min, max)
        elif w % min == 0:
            print(min, max)
        elif w % max == 0:
            print(min, max)
        else:
            print("UNSATISFIABLE")

if __name__ == '__main__':
    main()