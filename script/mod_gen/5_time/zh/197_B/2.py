def judge(s):
    if s == "#":
        return False
    else:
        return True
H, W, X, Y = map(int, input().split())
S = []
for i in range(H):
    S.append(input())
count = 1
for i in range(X-2, -1, -1):
    if judge(S[i][Y-1]):
        count += 1
    else:
        break
for i in range(X, H):
    if judge(S[i][Y-1]):
        count += 1
    else:
        break
for i in range(Y-2, -1, -1):
    if judge(S[X-1][i]):
        count += 1
    else:
        break
for i in range(Y, W):
    if judge(S[X-1][i]):
        count += 1
    else:
        break
print(count)

if __name__ == '__main__':
    judge()