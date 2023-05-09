def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    W.sort()
    ans = 0
    for x in range(1, N+1):
        if S[x-1] == '1':
            ans += N-x+1
        else:
            ans += x
    print(ans)

if __name__ == '__main__':
    main()