def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n == 1:
        print(a[0])
    else:
        for i in range(0, 4*n-1, 2):
            if a[i] != a[i+1]:
                print(a[i])
                break
        else:
            print(a[-1])

if __name__ == '__main__':
    main()