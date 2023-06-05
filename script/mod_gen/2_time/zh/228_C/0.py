def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a[x-1] = 0
    count = 1
    for i in range(n):
        if a[i] != 0:
            count += 1
    print(count)

if __name__ == '__main__':
    main()