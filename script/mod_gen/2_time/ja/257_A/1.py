def main():
    N, X = map(int, input().split())
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ans = ''
    for i in range(N):
        ans += alphabet[(X - 1) % 26]
        X = (X - 1) // 26
    print(ans[::-1])

if __name__ == '__main__':
    main()