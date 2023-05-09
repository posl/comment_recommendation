def main():
    N = int(input())
    C = input()
    W = [0] * N
    R = [0] * N
    for i in range(N):
        if C[i] == 'W':
            W[i] = W[i-1] + 1
            R[i] = R[i-1]
        else:
            W[i] = W[i-1]
            R[i] = R[i-1] + 1
    ans = N
    for i in range(N):
        ans = min(ans, W[i] + R[N-1] - R[i])
    print(ans)
