def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = list(map(int, input().split()))
        A.append(a)
        B.append(b)
    min_time = 10 ** 9
    for i in range(N):
        for j in range(N):
            if i == j:
                min_time = min(min_time, A[i] + B[j])
            else:
                min_time = min(min_time, max(A[i], B[j]))
    print(min_time)
