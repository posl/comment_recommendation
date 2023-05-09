def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    C = []
    for i in range(N):
        B.append([A[i] % 200, i])
    B.sort()
    for i in range(N-1):
        if B[i][0] == B[i+1][0]:
            C.append(B[i][1]+1)
            C.append(B[i+1][1]+1)
            break
    if len(C) == 0:
        print('No')
    else:
        print('Yes')
        print(len(C))
        print(*C)
        print(len(C))
        print(*C)
