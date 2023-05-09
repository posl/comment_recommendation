def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = [A[0]]
    for i in range(1, N):
        if A[i] != A[i - 1]:
            B.append(A[i])
    C = [0] * len(B)
    for i in range(N):
        if A[i] == B[0]:
            C[0] += 1
        elif A[i] == B[-1]:
            C[-1] += 1
        else:
            for j in range(len(B) - 1):
                if A[i] == B[j]:
                    C[j] += 1
    ans = 0
    for i in range(len(B)):
        ans += C[i] * (N - C[i])
    print(ans // 2)
