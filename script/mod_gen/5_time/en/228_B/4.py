def main():
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    count = 1
    for i in range(n):
        if i+1 == x:
            continue
        if a[i] == x:
            count += 1
            continue
        if a[a[i]-1] == x:
            count += 1
    print(count)

if __name__ == '__main__':
    main()