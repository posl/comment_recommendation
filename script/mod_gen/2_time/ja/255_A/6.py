def main():
    r,c = map(int,input().split())
    a = [list(map(int,input().split())) for i in range(2)]
    print(a[r-1][c-1])
main()

if __name__ == '__main__':
    main()