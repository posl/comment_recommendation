def main():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    for j in range(n):
        if x == a[j] or x == b[j]:
            print("Yes")
            break
        else:
            print("No")
            break

if __name__ == '__main__':
    main()