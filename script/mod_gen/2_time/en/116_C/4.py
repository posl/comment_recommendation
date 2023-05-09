def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    for h in H:
        ans += h
    print(ans)

if __name__ == '__main__':
    main()