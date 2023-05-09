def make_palindrome(N, A, B, S):
    if N % 2 == 0:
        half = N // 2
        if S[:half] == S[half:]:
            return A * N
        else:
            return A * N + B
    else:
        half = N // 2
        if S[:half] == S[half+1:]:
            return A * N
        else:
            return A * N + B
