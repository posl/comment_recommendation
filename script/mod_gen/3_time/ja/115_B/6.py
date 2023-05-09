def main():
    n = int(input())
    p = [int(input()) for i in range(n)]
    p.sort()
    print(sum(p[0:n-1]) + int(p[n-1]/2))

if __name__ == '__main__':
    main()