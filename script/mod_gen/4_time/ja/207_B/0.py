def main():
    A, B, C, D = map(int, input().split())
    if B >= C * D:
        print(-1)
        return
    ans = 0
    while A > 0:
        A -= B
        ans += 1
        A += C
    print(ans)

if __name__ == '__main__':
    main()