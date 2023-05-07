def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    min = 100000
    for i in range(N):
        for j in range(N):
            if i == j:
                if A[i] + B[j] < min:
                    min = A[i] + B[j]
            else:
                if max(A[i],B[j]) < min:
                    min = max(A[i],B[j])
    print(min)
