def main():
    N = int(input())
    p = [int(input()) for _ in range(N)]
    p.sort(reverse=True)
    print(sum(p[1:]) + p[0] // 2)

if __name__ == '__main__':
    main()