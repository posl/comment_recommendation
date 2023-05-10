def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A_sorted = sorted(A)
    for i in range(N-K):
        if A_sorted[i] != A_sorted[i+K]:
            print("Yes")
        else:
            print("No")
