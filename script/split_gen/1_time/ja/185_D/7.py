def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A + [N+1]
    #print(A)
    B = []
    for i in range(M+1):
        if A[i+1]-A[i]-1 > 0:
            B.append(A[i+1]-A[i]-1)
    #print(B)
    if len(B) == 0:
        print(0)
        exit()
    if len(B) == 1:
        print(1)
        exit()
    C = []
    for i in range(len(B)-1):
        C.append(B[i]+B[i+1])
    #print(C)
    print(min(C))
