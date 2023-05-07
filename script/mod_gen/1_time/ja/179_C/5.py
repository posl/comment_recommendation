def main():
    N = int(input())
    ans = 0
    for A in range(1, N):
        for B in range(1, N):
            if A*B + B >= N:
                break
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()