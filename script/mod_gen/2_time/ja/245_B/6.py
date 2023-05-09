def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n):
        if a[i] != i:
            print(i)
            return
    print(n)

if __name__ == '__main__':
    main()