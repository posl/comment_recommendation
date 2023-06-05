def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    a.append(a[0] + 360)
    a.append(a[1] + 360)
    max = 0
    for i in range(n):
        if a[i + 2] - a[i] > max:
            max = a[i + 2] - a[i]
    print(360 - max)

if __name__ == '__main__':
    main()