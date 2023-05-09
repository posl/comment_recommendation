def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if P[i] == i:
            ans += 1
    print(ans + (ans % 2))

if __name__ == '__main__':
    main()