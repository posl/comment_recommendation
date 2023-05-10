def main():
    import sys
    from collections import Counter
    input = sys.stdin.readline
    N = int(input())
    S = input().strip()
    c = Counter(S)
    r = c['R']
    g = c['G']
    b = c['B']
    ans = r * g * b
    for i in range(N):
        for j in range(i+1, N):
            k = j + (j - i)
            if k >= N:
                break
            if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
                ans -= 1
    print(ans)
