def main():
    N = int(input())
    ans = 0
    for a in range(1, int(N ** 0.5) + 1):
        for b in range(a, int(N ** 0.5) + 1):
            for c in range(b, int(N ** 0.5) + 1):
                if a * b * c <= N:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()