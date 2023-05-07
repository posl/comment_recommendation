def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # sort by deadline
    for i in range(N):
        for j in range(i+1, N):
            if B[i] > B[j]:
                B[i], B[j] = B[j], B[i]
                A[i], A[j] = A[j], A[i]
    # check if can complete all jobs in time
    time = 0
    for i in range(N):
        time += A[i]
        if time > B[i]:
            print("No")
            return
    print("Yes")
