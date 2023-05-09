def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S = [sorted(s) for s in S]
    S = [''.join(s) for s in S]
    S = sorted(S)
    ans = 0
    i = 0
    while i < N:
        j = i
        while j < N and S[i] == S[j]:
            j += 1
        ans += (j - i) * (j - i - 1) // 2
        i = j
    print(ans)
