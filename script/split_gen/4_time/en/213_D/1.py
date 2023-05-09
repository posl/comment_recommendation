def main():
    N = int(input())
    A = [0] * (N-1)
    B = [0] * (N-1)
    for i in range(N-1):
        A[i], B[i] = map(int, input().split())
    ans = [1]
    for i in range(N-1):
        if A[i] == ans[-1]:
            ans.append(B[i])
        elif B[i] == ans[-1]:
            ans.append(A[i])
    print(*ans, sep=' ')
