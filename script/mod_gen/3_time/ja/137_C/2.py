def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if S[i] == S[j]:
                continue
            if len(S[i]) != len(S[j]):
                break
            if isAnagram(S[i], S[j]):
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()