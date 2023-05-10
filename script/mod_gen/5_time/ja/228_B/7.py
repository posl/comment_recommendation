def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [0] + a
    count = 0
    for i in range(1, n + 1):
        if a[i] == x:
            count += 1
            x = i
    print(count)

if __name__ == '__main__':
    main()