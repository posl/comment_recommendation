def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    #print(len(A))
    #print(len(A) + 1)
    #print(len(A) + 1)
    #print([0] * (len(A) + 1))
    B = [0] * (len(A) + 1)
    #print(B)
    for i in range(1, len(A)):
        B[A[i]] += 1
    #print(B)
    for i in range(1, len(B)):
        print(B[i])
