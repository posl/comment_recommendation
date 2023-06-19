def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    min_num = 300
    for i in range(n):
        if a[i] >= x and b[i] >= y:
            if a[i] + b[i] < min_num:
                min_num = a[i] + b[i]
    if min_num == 300:
        print(-1)
    else:
        print(min_num)

if __name__ == '__main__':
    main()