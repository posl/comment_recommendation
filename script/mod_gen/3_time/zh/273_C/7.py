def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    k = 0
    for i in range(n):
        if i == 0:
            print(0)
        else:
            if a[i] != a[i-1]:
                k += 1
            print(k)

if __name__ == '__main__':
    main()