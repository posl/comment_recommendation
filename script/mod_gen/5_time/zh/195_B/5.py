def main():
    a, b, w = map(int, input().split())
    w *= 1000
    max_num = int(w / a)
    min_num = int(w / b)
    if min_num > max_num:
        print('UNSATISFIABLE')
    else:
        print(min_num, max_num)

if __name__ == '__main__':
    main()