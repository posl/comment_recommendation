def main():
    A, B, C, D = map(int, input().split())
    if A > B * D:
        print(-1)
        exit()
    if B <= C:
        print(-1)
        exit()
    if B <= D * C:
        print(-1)
        exit()
    ans = 0
    while A > B * D:
        A += B
        A -= C * D
        ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()