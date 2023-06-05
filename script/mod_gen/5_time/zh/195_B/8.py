def main():
    a, b, w = map(int, input().split())
    w *= 1000
    min = 0
    max = 0
    for i in range(a, b+1):
        if w % i == 0:
            if min == 0:
                min = w // i
            max = w // i
    if min == 0:
        print("UNSATISFIABLE")
    else:
        print(min, max)

if __name__ == '__main__':
    main()