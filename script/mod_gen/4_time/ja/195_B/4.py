def main():
    a, b, w = map(int, input().split())
    w *= 1000
    max = 0
    min = 1000000000
    for i in range(1, w + 1):
        if a * i <= w and w <= b * i:
            if i > max:
                max = i
            if i < min:
                min = i
    if max == 0:
        print('UNSATISFIABLE')
    else:
        print(min, max)

if __name__ == '__main__':
    main()