def main():
    n,x,y = map(int,input().split())
    a = list(map(int,input().split()))
    a.append(abs(x))
    a.append(abs(y))
    a.sort()
    a.reverse()
    for i in range(n):
        if a[i] > a[i+1] + a[i+2]:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()