def main():
    N, X = map(int, input().split())
    S = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = ""
    for i in range(N):
        ans += S[(X-1)%26]
        X = (X-1)//26
    print(ans)

if __name__ == '__main__':
    main()