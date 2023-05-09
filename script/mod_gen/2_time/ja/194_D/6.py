def main():
    N = int(input())
    # print(N)
    ans = 0.0
    for i in range(1,N):
        ans += N/(N-i)
    print(ans)

if __name__ == '__main__':
    main()