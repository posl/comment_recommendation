def main():
    N, Q = map(int, input().split())
    S = input()
    S = S.replace("AC", "X")
    S = S.replace("A", "0")
    S = S.replace("C", "0")
    S = S.replace("G", "0")
    S = S.replace("T", "0")
    S = S.replace("X", "1")
    S = list(map(int, S))
    for i in range(1, N):
        S[i] += S[i - 1]
    for _ in range(Q):
        l, r = map(int, input().split())
        print(S[r - 1] - S[l - 1])
