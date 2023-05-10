def main():
    n = int(input())
    left = 1
    right = 2*n+1
    while True:
        mid = (left+right)//2
        print(mid)
        flush()
        aoki = int(input())
        if aoki == 0:
            break
        elif aoki == -1:
            right = mid
        elif aoki == 1:
            left = mid
    exit()

if __name__ == '__main__':
    main()