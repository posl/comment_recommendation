def main():
    n = int(input())
    d = list(map(int,input().split()))
    d.sort()
    if n % 2 == 0:
        print(d[n//2] - d[n//2 - 1])
    else:
        print(0)

if __name__ == '__main__':
    main()