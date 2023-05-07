def main():
    N = int(input())
    ans = 0
    for i in range(10):
        for j in range(10):
            ans += (N//10 + (1 if i <= N % 10 else 0)) * (N//10 + (1 if j <= N % 10 else 0))
    print(ans)

if __name__ == '__main__':
    main()