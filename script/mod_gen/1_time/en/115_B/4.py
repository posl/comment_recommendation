def main():
    N = int(input())
    p = [int(input()) for _ in range(N)]
    p.sort(reverse=True)
    p[0] //= 2
    print(sum(p))

if __name__ == '__main__':
    main()