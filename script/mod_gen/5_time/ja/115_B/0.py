def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    p.sort()
    print(sum(p[:-1]) + p[-1] // 2)

if __name__ == '__main__':
    main()