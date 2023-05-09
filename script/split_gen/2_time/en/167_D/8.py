def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # A[i] = i+1 -> A[i]-1 = i
    # 1-index -> 0-index
    A = [i-1 for i in A]
    #print(A)
    #print(N, K)
    #print(A)
    #print(A[0])
    #print(A[A[0]])
    #print(A[A[A[0]]])
    #print(A[A[A[A[0]]]])
    #print(A[A[A[A[A[0]]]]])
    #print(A[A[A[A[A[A[0]]]]]])
    #print(A[A[A[A[A[A[A[0]]]]]]])
    #print(A[A[A[A[A[A[A[A[0]]]]]]]])
    #print(A[A[A[A[A[A[A[A[A[0]]]]]]]]])
    #print(A[A[A[A[A[A[A[A[A[A[0]]]]]]]]]])
