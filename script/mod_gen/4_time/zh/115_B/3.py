def main():
    n = int(input())
    p = [int(input()) for i in range(n)]
    p.sort()
    print(int(sum(p) - p[-1]/2))

if __name__ == '__main__':
    main()