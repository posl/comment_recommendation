def flip(S):
    n = len(S)
    return S[n:]+S[:n]
N = int(input())
S = input()
Q = int(input())
flipped = False
for _ in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        if flipped:
            A = (A + N) % (2*N)
            B = (B + N) % (2*N)
        S = S[:A-1] + S[B-1] + S[A:B-1] + S[A-1] + S[B:]
    else:
        flipped = not flipped

if __name__ == '__main__':
    flip()