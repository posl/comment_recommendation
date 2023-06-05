def main():
    n,m = map(int,input().split())
    s = [[0 for i in range(2)] for j in range(m)]
    for i in range(m):
        s[i] = map(int,input().split())
    print(s)

if __name__ == '__main__':
    main()