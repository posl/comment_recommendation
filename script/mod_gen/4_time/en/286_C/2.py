def main():
    N,A,B = map(int,input().split())
    S = input()
    ans = 0
    for i in range(N//2):
        if S[i] == S[-i-1]:
            continue
        if S[i] == 'a':
            ans += A
        elif S[i] == 'b':
            ans += B
        else:
            print(-1)
            return
    if N % 2 == 1 and S[N//2] != 'a' and S[N//2] != 'b':
        print(-1)
        return
    print(ans)

if __name__ == '__main__':
    main()