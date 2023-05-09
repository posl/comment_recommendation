def main():
    n = int(input())
    a = list(map(int, input().split()))
    while len(a) > 1:
        a.sort()
        if a[-1] != a[-2]:
            a[-1] -= a[-2]
            a.pop(-2)
        else:
            a.pop(-1)
    print(a[0])

if __name__ == '__main__':
    main()