def main():
    l, r = map(int, input().split())
    if r - l >= 2019:
        print(0)
        return
    else:
        ans = 2019
        for i in range(l, r):
            for j in range(i+1, r+1):
                if ans > (i*j) % 2019:
                    ans = (i*j) % 2019
        print(ans)
        return

if __name__ == '__main__':
    main()