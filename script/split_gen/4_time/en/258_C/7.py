def main():
    N, Q = map(int, input().split())
    S = input()
    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            S = S[-q[1]:] + S[:-q[1]]
        elif q[0] == 2:
            print(S[q[1]-1])
