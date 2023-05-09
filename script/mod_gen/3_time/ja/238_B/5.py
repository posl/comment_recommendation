def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = a * 2
    max = 0
    for i in range(n):
        tmp = 0
        for j in range(n):
            tmp += a[i+j]
            if tmp > max:
                max = tmp
    print(360-max)

if __name__ == '__main__':
    main()