def main():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p.sort()
    print(sum(p[:-1]) + p[-1] // 2)

if __name__ == '__main__':
    main()