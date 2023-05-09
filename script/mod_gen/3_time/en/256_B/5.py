def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        if i == 0:
            p += 1
        else:
            p += a[i-1] + 1
            if p >= 4:
                p -= 4
    print(p)

if __name__ == '__main__':
    main()