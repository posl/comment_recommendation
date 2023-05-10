def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    if n == 0:
        print(x)
        return
    min_diff = 1000
    min_num = 0
    for i in range(102):
        if i in p:
            continue
        diff = abs(x - i)
        if diff < min_diff:
            min_diff = diff
            min_num = i
    print(min_num)

if __name__ == '__main__':
    main()