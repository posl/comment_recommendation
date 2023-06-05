def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if p[i] == (i - 1) % N or p[i] == i or p[i] == (i + 1) % N:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()