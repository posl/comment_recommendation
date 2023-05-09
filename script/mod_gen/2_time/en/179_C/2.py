def main():
    N = int(input())
    ans = 0
    for b in range(1, N):
        ans += (N - 1) // b
    print(ans)

if __name__ == '__main__':
    main()