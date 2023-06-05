def main():
    n = int(raw_input())
    a = map(int, raw_input().split())
    a.sort()
    a.append(a[0] + 360)
    max = 0
    for i in range(n):
        if a[i + 1] - a[i] > max:
            max = a[i + 1] - a[i]
    print 360 - max

if __name__ == '__main__':
    main()