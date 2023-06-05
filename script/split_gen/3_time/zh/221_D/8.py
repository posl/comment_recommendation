def main():
    N = int(input())
    #print(N)
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    dict = {}
    for i in range(N):
        for j in range(B[i]):
            if A[i]+j in dict:
                dict[A[i]+j] += 1
            else:
                dict[A[i]+j] = 1
    #print(dict)
    for i in range(N):
        if i == N-1:
            print(dict[i+1])
        else:
            print(dict[i+1], end=" ")
