def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i % 2 == 0:
            continue
        if N % i == 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()