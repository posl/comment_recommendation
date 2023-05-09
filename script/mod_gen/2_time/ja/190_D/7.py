def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if (N-i+1) % i == 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()