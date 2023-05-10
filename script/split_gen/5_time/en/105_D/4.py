def read_ints():
    return list(map(int, input().split()))
N, M = read_ints()
A = read_ints()
S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = (S[i] + A[i]) % M
from collections import Counter
C = Counter(S)
ans = 0
for k, v in C.items():
    ans += v * (v - 1) // 2
print(ans)
