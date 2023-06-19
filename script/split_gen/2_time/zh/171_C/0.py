def solution(N):
    if N <= 26:
        return chr(ord('a') + N - 1)
    else:
        return solution((N-1) // 26) + solution((N-1) % 26 + 1)
