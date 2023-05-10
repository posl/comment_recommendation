def main():
    n,m = map(int, input().split())
    a = []
    for i in range(m):
        a.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(i+1,n):
            if not (i+1 in a[j-1]):
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()