def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    min_time = 10**10
    for i in range(N):
        for j in range(N):
            if i == j:
                min_time = min(min_time, A[i] + B[j])
            else:
                min_time = min(min_time, max(A[i], B[j]))
    print(min_time)
