def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    C = [0] * (10 ** 9 + 2)
    for i in range(N):
        C[A[i]] += 1
        C[A[i] + B[i]] -= 1
    for i in range(10 ** 9 + 1):
        C[i + 1] += C[i]
    for i in range(1, N + 1):
        ans = 0
        for j in range(10 ** 9 + 1):
            if C[j] == i:
                ans += 1
        print(ans, end = " ")
    print()
