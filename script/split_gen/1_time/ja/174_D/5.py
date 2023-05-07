def input():
    return open(0).readline()
N = int(input())
S = input().strip()
ans = 0
for i in range(N):
    if S[i] == 'R':
        for j in range(i+1,N):
            if S[j] == 'W':
                ans += 1
                S = S[:i] + 'W' + S[i+1:j] + 'R' + S[j+1:]
                break
print(ans)
