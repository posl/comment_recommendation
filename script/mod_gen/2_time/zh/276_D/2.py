def main():
    n = int(input())
    a = list(map(int,input().split()))
    count = 0
    while True:
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] = a[i] / 2
            elif a[i] % 3 == 0:
                a[i] = a[i] / 3
            else:
                break
        else:
            count += 1
            continue
        break
    if count == 0:
        print(-1)
    else:
        print(count)
main()
#解答1

if __name__ == '__main__':
    main()