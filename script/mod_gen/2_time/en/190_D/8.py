def main():
    N = int(input())
    n = int((N*2)**0.5)
    print(n)
    count = 0
    while n*(n+1)//2 <= N:
        count += 1
        n += 1
    print(count)

if __name__ == '__main__':
    main()