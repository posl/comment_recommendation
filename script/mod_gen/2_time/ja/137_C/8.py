def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.sort()
    #print(S)
    ans = 0
    for i in range(N-1):
        for j in range(i+1,N):
            if S[i] == S[j]:
                continue
            else:
                if sorted(S[i]) == sorted(S[j]):
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()