def main():
    n,m = map(int,input().split())
    b = []
    for i in range(n):
        b.append(list(map(int,input().split())))
    for i in range(10**100):
        for j in range(7):
            if b == [[(i*7+j+1)+k*7 for k in range(m)] for i in range(n)]:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()