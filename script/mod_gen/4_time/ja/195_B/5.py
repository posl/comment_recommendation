def main():
    a,b,w = map(int, input().split())
    w *= 1000
    min = 10000000
    max = 0
    for i in range(1, 1000001):
        if a * i <= w <= b * i:
            if min > i:
                min = i
            if max < i:
                max = i
    if max == 0:
        print('UNSATISFIABLE')
    else:
        print(min, max)

if __name__ == '__main__':
    main()