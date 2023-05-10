def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    for i in range(K):
        if A[i] > A[B[i]-1]:
            print("Yes")
            return 0
    print("No")
    return 0
