def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, A)
    #print(A)
    A.sort()
    #print(A)
    for i in range(N-K):
        if A[i] == A[i+K]:
            print("No")
            return
    print("Yes")
    return
