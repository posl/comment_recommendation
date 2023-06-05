def base_n_to_10(X, n):
    out = 0
    for i in range(len(X)):
        out += int(X[i]) * n ** (len(X) - 1 - i)
    return out
X = input()
M = int(input())
d = 0
for i in range(len(X)):
    d = max(d, int(X[i]))
l = d + 1
r = 10 ** 18 + 1
while r - l > 1:
    m = (r + l) // 2
    if base_n_to_10(X, m) <= M:
        l = m
    else:
        r = m
print(l - d)

if __name__ == '__main__':
    base_n_to_10()