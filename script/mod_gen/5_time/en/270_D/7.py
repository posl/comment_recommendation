def main():
    n,k = map(int, input().split())
    a = [int(i) for i in input().split()]
    cnt = 0
    while n > 0:
        if n >= a[-1]:
            n -= a[-1]
            cnt += 1
        else:
            a.pop()
    print(cnt)

if __name__ == '__main__':
    main()