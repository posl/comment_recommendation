def main():
    p = list(map(int,input().split()))
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    ans = ''
    for i in p:
        ans += alpha[i-1]
    print(ans)

if __name__ == '__main__':
    main()