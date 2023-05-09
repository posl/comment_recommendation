def main():
    N, Q = map(int, input().split())
    S = input()
    for _ in range(Q):
        t, x = input().split()
        x = int(x)
        if t == '1':
            S = S[N-x:] + S[:N-x]
        else:
            print(S[x-1])
