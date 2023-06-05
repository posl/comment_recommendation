def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    tmp = 0
    for i in range(1,n):
        if h[i-1] >= h[i]:
            tmp += 1
        else:
            if tmp > count:
                count = tmp
            tmp = 0
    if tmp > count:
        count = tmp
    print(count)

if __name__ == '__main__':
    main()