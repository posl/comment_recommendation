def main():
    N, K = (int(x) for x in input().split())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    if N == 1:
        if abs(A[0] - B[0]) <= K:
            print("Yes")
        else:
            print("No")
        return
    for i in range(N):
        if abs(A[i] - B[i]) > K:
            print("No")
            return
    print("Yes")
