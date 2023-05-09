def main():
    N, Q = map(int, input().split())
    S = input()
    S = S[::-1]
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            S = S[1:] + S[0]
        else:
            print(S[N-x])
