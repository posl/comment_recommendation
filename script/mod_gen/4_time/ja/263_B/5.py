def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if (i+1) == P[i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()