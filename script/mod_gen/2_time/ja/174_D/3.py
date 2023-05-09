def main():
    N = int(input())
    c = list(input())
    ans = 0
    for i in range(N):
        if c[i] == 'R':
            ans += 1
    print(min(ans, N - ans))

if __name__ == '__main__':
    main()