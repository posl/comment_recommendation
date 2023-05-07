def main():
    # input
    n = int(input())
    a = list(map(int, input().split()))
    # compute
    a.sort()
    if a[0] == 0:
        print(-1)
    else:
        print(a[-1] + a[-2])
    # output

if __name__ == '__main__':
    main()