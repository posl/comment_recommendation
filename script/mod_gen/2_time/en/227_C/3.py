def main():
    N = int(input())
    ans = 0
    for c in range(1, int(N ** 0.5) + 1):
        for b in range(1, c + 1):
            for a in range(1, b + 1):
                if a * b * c <= N:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()