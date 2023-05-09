def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    if N % A == 0:
        ans = 4 + N // A
    else:
        ans = 4 + N // A + 1
    if N % B == 0:
        ans = min(ans, 3 + N // B)
    else:
        ans = min(ans, 3 + N // B + 1)
    if N % C == 0:
        ans = min(ans, 2 + N // C)
    else:
        ans = min(ans, 2 + N // C + 1)
    if N % D == 0:
        ans = min(ans, 1 + N // D)
    else:
        ans = min(ans, 1 + N // D + 1)
    if N % E == 0:
        ans = min(ans, N // E)
    else:
        ans = min(ans, N // E + 1)
    print(ans)
