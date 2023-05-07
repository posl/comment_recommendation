def main():
    n,k = map(int,input().split())
    s = [input() for i in range(n)]
    print(solve(n,k,s))

if __name__ == '__main__':
    main()