def main():
    n = int(input())
    ans = 0
    for i in range(1,n):
        ans += n/(n-i)
    print(ans)

if __name__ == '__main__':
    main()