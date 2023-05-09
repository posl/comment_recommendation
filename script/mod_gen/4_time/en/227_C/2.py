def main():
    N = int(input())
    ans = 0
    for a in range(1, N+1):
        for b in range(a, N+1):
            for c in range(b, N+1):
                if a*b*c <= N:
                    ans += 1
                else:
                    break
    print(ans)

if __name__ == '__main__':
    main()