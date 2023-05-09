def main():
    H, A = map(int, input().split())
    ans = 0
    while H > 0:
        H -= A
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()