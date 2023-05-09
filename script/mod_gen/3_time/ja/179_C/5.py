def main():
    N = int(input())
    ans = 0
    for A in range(1, N):
        for B in range(1, N):
            if A * B < N:
                ans += 1
            else:
                break
    print(ans)

if __name__ == '__main__':
    main()