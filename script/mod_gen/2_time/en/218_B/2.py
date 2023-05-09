def main():
    P = list(map(int, input().split()))
    S = [chr(i) for i in range(97, 123)]
    ans = ''
    for i in P:
        ans += S[i-1]
    print(ans)

if __name__ == '__main__':
    main()