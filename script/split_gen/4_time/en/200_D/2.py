def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    C = []
    for i in range(N):
        B.append(A[i] % 200)
    for i in range(N):
        C.append(A[i] % 200)
    for i in range(N):
        for j in range(i+1,N):
            if B[i] == B[j]:
                print("Yes")
                print(2)
                print(i+1,j+1)
                print(1)
                print(i+1)
                return 0
            if C[i] == C[j]:
                print("Yes")
                print(1)
                print(i+1)
                print(2)
                print(i+1,j+1)
                return 0
    print("No")
    return 0
