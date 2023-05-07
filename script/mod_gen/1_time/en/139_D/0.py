def main():
    N = int(input())
    if N == 1:
        print(0)
        return
    ans = 0
    for i in range(1, N):
        ans += (N - 1) // i
    print(ans)

if __name__ == '__main__':
    main()