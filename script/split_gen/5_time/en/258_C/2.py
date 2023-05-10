def main():
    N, Q = map(int, input().split())
    S = input()
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            S = S[N-x:] + S[0:N-x]
        else:
            print(S[x-1])
