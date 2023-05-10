def main():
    n,x = map(int,input().split())
    ans = ''
    for i in range(n):
        ans += chr(i+65)*n
    print(ans[x-1])

if __name__ == '__main__':
    main()