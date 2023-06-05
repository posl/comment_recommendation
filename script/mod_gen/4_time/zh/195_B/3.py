def main():
    a, b, w = map(int, input().split())
    w *= 1000
    min = w // b
    if w % b != 0:
        min += 1
    max = w // a
    if w % a != 0:
        max += 1
    if min > max:
        print("UNSATISFIABLE")
    else:
        print(min, max)

if __name__ == '__main__':
    main()