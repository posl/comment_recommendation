def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    while len(a) > 1:
        m = a[0]
        for i in range(1, len(a)):
            m %= a[i]
            if m == 0:
                break
        if m == 0:
            a.pop(0)
        else:
            break
    print(a[0])

if __name__ == '__main__':
    main()