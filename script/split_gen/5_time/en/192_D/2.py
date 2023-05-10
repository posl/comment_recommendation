def baseN(num, b):
    return ((num == 0) and "0") or (baseN(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])
X = input()
M = int(input())
d = max([int(c) for c in X])
ans = 0
while True:
    try:
        n = baseN(M, d+1)
        if len(n) > len(X):
            break
        ans += 1
        M += 1
    except:
        break
print(ans)
