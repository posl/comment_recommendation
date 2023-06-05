def getStr(A, B, K):
    if A == 0:
        return "b"*B
    if B == 0:
        return "a"*A
    if K <= 1:
        return "a"*A + "b"*B
    if K > 1:
        return getStr(A-1, B, K-1) + getStr(A, B-1, K-1)
A, B, K = map(int, input().split())
print(getStr(A, B, K))
