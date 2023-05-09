def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a.sort()
    max1 = a[-1]
    max2 = a[-2]
    for i in range(n):
        if a[i] == max1:
            print(max2)
        else:
            print(max1)

if __name__ == '__main__':
    main()