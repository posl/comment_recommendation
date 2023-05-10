def main():
    n,m = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(m)]
    print(n,m,ab)

if __name__ == '__main__':
    main()