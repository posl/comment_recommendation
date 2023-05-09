def main():
    N, K = map(int, input().split())
    ans = 0
    if N % K != 0:
        ans = 1
    print(ans)

if __name__ == '__main__':
    main()