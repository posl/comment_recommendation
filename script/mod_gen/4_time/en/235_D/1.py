def main():
    a, n = map(int, input().split())
    if n == 1:
        print(0)
        return
    if a == 1:
        print(n-1)
        return
    x = 1
    for i in range(n):
        x = x * a
        if x >= n:
            print(i+1)
            return
    print(-1)
    return

if __name__ == '__main__':
    main()