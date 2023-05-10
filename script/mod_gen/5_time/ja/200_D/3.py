def main():
    n = int(input())
    a = list(map(int,input().split()))
    if n == 2:
        if a[0] % 200 == a[1] % 200:
            print("Yes")
            print("1 1")
            print("1 2")
            return
        else:
            print("No")
            return
    elif n == 3:
        if a[0] % 200 == a[1] % 200:
            print("Yes")
            print("1 1")
            print("2 2 3")
            return
        elif a[0] % 200 == a[2] % 200:
            print("Yes")
            print("1 1")
            print("2 2 3")
            return
        elif a[1] % 200 == a[2] % 200:
            print("Yes")
            print("1 2")
            print("2 1 3")
            return
        else:
            print("No")
            return
    else:
        for i in range(n):
            for j in range(i+1,n):
                if a[i] % 200 == a[j] % 200:
                    print("Yes")
                    print("1",i+1)
                    print("1",j+1)
                    return
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if a[i] % 200 + a[j] % 200 == a[k] % 200:
                        print("Yes")
                        print("2",i+1,j+1)
                        print("1",k+1)
                        return
        print("No")
        return
main()

if __name__ == '__main__':
    main()