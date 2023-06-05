def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x-1] = 0
    a.sort()
    for i in range(n):
        if a[i] == 0:
            print(i)
            break
    else:
        print(n)

if __name__ == '__main__':
    main()