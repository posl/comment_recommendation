def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if max(A) in [A[i] for i in B]:
        print("Yes")
    else:
        print("No")
    return 0
