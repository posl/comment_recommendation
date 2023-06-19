def main():
    a = [int(i) for i in input().split()]
    a.sort()
    res = 1
    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            res += 1
    print(res)

if __name__ == '__main__':
    main()