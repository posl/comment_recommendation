def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    if N < M:
        print("No")
        return
    for i in range(M):
        if B[i] > A[i]:
            print("No")
            return
    print("Yes")
