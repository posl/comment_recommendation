def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if i == 0:
            ans += 1
        else:
            if P[i] <= min(P[:i+1]):
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()