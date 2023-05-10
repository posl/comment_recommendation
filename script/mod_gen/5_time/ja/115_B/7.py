def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    p.sort(reverse=True)
    print(int(sum(p) - p[0]/2))

if __name__ == '__main__':
    main()