def main():
    P = list(map(int, input().split()))
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ans = ''
    for i in P:
        ans += alphabet[i-1]
    print(ans)
main()
