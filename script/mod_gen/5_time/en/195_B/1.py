def main():
    a, b, w = map(int, input().split())
    w *= 1000
    min_count = 0
    max_count = 0
    for i in range(1, w+1):
        if a*i <= w and w <= b*i:
            min_count = i
            break
    for i in range(w, 0, -1):
        if a*i <= w and w <= b*i:
            max_count = i
            break
    if min_count == 0 or max_count == 0:
        print('UNSATISFIABLE')
    else:
        print(min_count, max_count)
    return

if __name__ == '__main__':
    main()