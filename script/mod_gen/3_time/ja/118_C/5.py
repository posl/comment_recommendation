def main():
    n = int(input())
    a = list(map(int, input().split()))
    while True:
        a.sort()
        a = list(set(a))
        if len(a) == 1:
            break
        else:
            a[-1] = a[-1] % a[0]
            if a[-1] == 0:
                a.pop()
    print(a[0])

if __name__ == '__main__':
    main()