def solution(N, M, T, A, B):
    battery = N
    for i in range(M):
        battery -= (A[i] - B[i-1])
        if battery <= 0:
            return False
        battery += (B[i] - A[i])
        if battery > N:
            battery = N
    battery -= (T - B[-1])
    if battery <= 0:
        return False
    return True

if __name__ == '__main__':
    solution()