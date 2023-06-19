def main():
    n = int(input())
    a = list(map(int, input().split()))
    while len(a) > 1:
        a.sort()
        a[-1] -= a[0]
        a.pop(0)
        if a[-1] == 0:
            a.pop()
    print(a[0])

if __name__ == '__main__':
    main()