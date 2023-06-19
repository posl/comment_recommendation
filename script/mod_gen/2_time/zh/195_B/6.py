def main():
    a, b, w = map(int, input().split())
    w *= 1000
    min_num = w // b
    max_num = w // a
    if min_num > max_num:
        print('UNSATISFIABLE')
    else:
        print(min_num, max_num)

if __name__ == '__main__':
    main()