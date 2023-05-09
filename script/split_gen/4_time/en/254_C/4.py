def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N-1):
        if A[i] > A[i+1]:
            if i+K < N:
                if A[i] > A[i+K]:
                    print("No")
                    return
            else:
                if A[i] > A[-1]:
                    print("No")
                    return
    print("Yes")
