def get_score(s):
    if s == 'r':
        return R
    elif s == 's':
        return S
    else:
        return P
N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
score = 0
for i in range(N):
    if i >= K and T[i] == T[i-K] and T[i] == T[i-K]:
        continue
    score += get_score(T[i])
print(score)
