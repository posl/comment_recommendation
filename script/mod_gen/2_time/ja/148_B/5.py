def main():
    N = int(input())
    S, T = input().split()
    ans = ''
    for i in range(N):
        ans += S[i]
        ans += T[i]
    print(ans)

if __name__ == '__main__':
    main()