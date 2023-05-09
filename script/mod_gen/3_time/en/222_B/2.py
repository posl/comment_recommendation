def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        if a < P:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()