def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = sorted(a)
    for i in range(n):
        if a[i] != b[i]:
            if (i+k) > n:
                print("No")
                exit()
            else:
                a[i],a[i+k] = a[i+k],a[i]
                if a[i] != b[i]:
                    print("No")
                    exit()
                else:
                    continue
        else:
            continue
    print("Yes")
    exit()

if __name__ == '__main__':
    main()