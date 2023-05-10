def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = A[K-1::]
    if A[K-1] == A[-1]:
        print("No")
        return
    if K == 1:
        print("Yes")
        return
    if len(B) == len(set(B)):
        print("Yes")
    else:
        print("No")
