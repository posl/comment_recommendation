def main():
    n,x,y = map(int,input().split())
    a = list(map(int,input().split()))
    a.append(abs(x))
    a.append(abs(y))
    a.sort()
    a.reverse()
    if a[0] == a[1]:
        print("No")
    else:
        for i in range(1,n+1):
            if a[i-1] == a[i]:
                print("No")
                break
        else:
            print("Yes")

if __name__ == '__main__':
    main()