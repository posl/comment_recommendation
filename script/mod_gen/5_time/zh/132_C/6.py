def main():
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    m = int(n/2)
    print(d[m]-d[m-1])

if __name__ == '__main__':
    main()