def main():
    N = int(input())
    ans = 0
    for k in range(1, N+1):
        if N % k == 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()