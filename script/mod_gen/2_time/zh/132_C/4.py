def main():
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    n1 = n//2
    n2 = n1-1
    print(d[n1]-d[n2])

if __name__ == '__main__':
    main()