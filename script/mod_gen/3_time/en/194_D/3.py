def main():
    N = int(input())
    ans = N
    for i in range(1, N):
        ans += i * (N / i)
    print(ans)

if __name__ == '__main__':
    main()