def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    if a[m-1]*4*m>=sum(a):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()