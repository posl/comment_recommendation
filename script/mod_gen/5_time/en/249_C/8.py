def main():
    N, K = map(int, input().split())
    S = []
    for i in range(N):
        S.append(input())
    alphabet = [0] * 26
    for i in range(N):
        for s in S[i]:
            alphabet[ord(s) - ord('a')] += 1
    ans = 0
    for i in range(1 << N):
        temp = [0] * 26
        for j in range(N):
            if i & (1 << j):
                for s in S[j]:
                    temp[ord(s) - ord('a')] += 1
        count = 0
        for j in range(26):
            if temp[j] > 0 and alphabet[j] == temp[j]:
                count += 1
        if count == K:
            ans = max(ans, sum(temp))
    print(ans)

if __name__ == '__main__':
    main()