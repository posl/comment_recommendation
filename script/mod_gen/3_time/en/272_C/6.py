def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    if a[-1] % 2 == 0:
        print(a[-1])
    else:
        if a[-2] % 2 == 0:
            print(a[-2])
        else:
            print(-1)

if __name__ == '__main__':
    main()