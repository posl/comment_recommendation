def main():
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    if n == 1:
        print("Yes")
    elif m == 1:
        for i in range(n-1):
            if a[i][0] != a[i+1][0]-1:
                print("No")
                return
        print("Yes")
    else:
        for i in range(n-1):
            for j in range(m-1):
                if a[i][j] != a[i+1][j+1]-1:
                    print("No")
                    return
        print("Yes")

if __name__ == '__main__':
    main()