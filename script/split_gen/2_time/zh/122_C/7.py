def main():
    N, Q = map(int, input().split())
    S = input()
    lr = []
    for i in range(Q):
        lr.append(list(map(int, input().split())))
    ac = [0] * N
    for i in range(1, N):
        if S[i - 1] == 'A' and S[i] == 'C':
            ac[i] = ac[i - 1] + 1
        else:
            ac[i] = ac[i - 1]
    for i in range(Q):
        print(ac[lr[i][1] - 1] - ac[lr[i][0] - 1])
