def main():
    a = list(map(int,input().split()))
    a.sort()
    ans = a[2] - a[0]
    print(ans)

if __name__ == '__main__':
    main()