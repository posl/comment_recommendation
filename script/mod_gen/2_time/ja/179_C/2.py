def main():
    N = int(input())
    ans = 0
    for A in range(1, N):
        for B in range(1, N):
            C = N - A * B
            if C > 0:
                ans += 1
            else:
                break
    print(ans)

if __name__ == '__main__':
    main()