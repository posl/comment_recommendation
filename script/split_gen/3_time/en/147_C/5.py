def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append([int(x) for x in input().split()])
    ans = 0
    for i in range(2**N):
        honest = []
        for j in range(N):
            if ((i >> j) & 1):
                honest.append(j+1)
        isOK = True
        for j in honest:
            for k in range(A[j-1][0]):
                if A[j-1][2*k+1] == 1:
                    if A[j-1][2*k+2] not in honest:
                        isOK = False
                        break
                else:
                    if A[j-1][2*k+2] in honest:
                        isOK = False
                        break
            if not isOK:
                break
        if isOK:
            ans = max(ans, len(honest))
    print(ans)
