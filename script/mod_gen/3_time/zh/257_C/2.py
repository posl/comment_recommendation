def f(x):
    y = 0
    for i in range(N):
        if S[i] == "0" and x > W[i]:
            y += 1
        elif S[i] == "1" and x <= W[i]:
            y += 1
    return y
N = int(input())
S = input()
W = list(map(int, input().split()))
l = 0
r = 10 ** 9 + 1
while l + 1 < r:
    m = (l + r) // 2
    if f(m) == N:
        l = m
    else:
        r = m
print(l)

if __name__ == '__main__':
    f()