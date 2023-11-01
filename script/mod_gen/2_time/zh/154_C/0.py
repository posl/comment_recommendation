def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    for i in range(0,n-1):
        if a[i]==a[i+1]:
            print

if __name__ == '__main__':
    main()