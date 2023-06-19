def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #print(N, K, A, B)
    #print(len(A), len(B))
    #print(A[0], A[1])
    #print(B[0], B[1])
    for i in range(N):
        if abs(A[i] - B[i]) > K:
            print("No")
            return
    print("Yes")
