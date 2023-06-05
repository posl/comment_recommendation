def main():
    n,k,x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if k == 0:
        print(sum(a))
    else:
        print(sum(a[0:n-k]) + k * x)

if __name__ == '__main__':
    main()