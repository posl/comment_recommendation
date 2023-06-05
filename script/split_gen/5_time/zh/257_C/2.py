def f(x):
    num = 0
    for i in range(len(S)):
        if S[i] == '0' and x > W[i]:
            num += 1
        elif S[i] == '1' and x <= W[i]:
            num += 1
    return num
N = int(input())
S = input()
W = list(map(int, input().split()))
max_w = max(W)
min_w = min(W)
while max_w - min_w > 1:
    mid = (max_w + min_w) // 2
    if f(mid) == N:
        break
    elif f(mid) < N:
        max_w = mid
    else:
        min_w = mid
print(mid)
