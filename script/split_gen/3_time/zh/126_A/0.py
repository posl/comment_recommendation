def change_char(s, p, r):
    return s[:p]+r+s[p+1:]
N, K = map(int, input().split())
S = input()
print(change_char(S, K-1, S[K-1].lower()))
