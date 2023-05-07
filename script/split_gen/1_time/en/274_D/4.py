def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    if x < min(A) or y < min(A):
        print("No")
        return
    for i in range(N - 1):
        for j in range(i + 1, N):
            if abs(A[i] - A[j]) == 1:
                print("No")
                return
    print("Yes")
