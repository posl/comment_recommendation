def main():
    N, X = map(int, input().split())
    ans = "No"
    pos = 0
    for i in range(N):
        a, b = map(int, input().split())
        pos += a
        if pos >= X:
            ans = "Yes"
            break
        pos += b
        if pos >= X:
            ans = "Yes"
            break
    print(ans)

if __name__ == '__main__':
    main()