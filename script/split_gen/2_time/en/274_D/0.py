def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        for j in range(i+1, N):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    A.append(x)
    A.append(y)
    for i in range(N):
        if A[i] > A[i+1]:
            print("No")
            return
    print("Yes")
