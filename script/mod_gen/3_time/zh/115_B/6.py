def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    p.sort()
    p[-1] = int(p[-1] / 2)
    print(sum(p))

if __name__ == '__main__':
    main()