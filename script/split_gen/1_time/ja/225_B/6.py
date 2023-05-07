def main():
    N = int(input())
    A = []
    B = []
    for i in range(N-1):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    A.sort()
    B.sort()
    #print(A)
    #print(B)
    if A[0] == 1 and B[N-2] == N:
        print("Yes")
    else:
        print("No")
