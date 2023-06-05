def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n-k+1):
        print(max(a[i:i+k]))

if __name__ == '__main__':
    main()