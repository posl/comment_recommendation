def main():
    N, Q = map(int, input().split())
    S = input()
    lrs = [list(map(int, input().split())) for _ in range(Q)]
    ac = [0] * N
    for i in range(1, N):
        ac[i] = ac[i-1]
        if S[i-1:i+1] == 'AC':
            ac[i] += 1
    for lr in lrs:
        print(ac[lr[1]-1] - ac[lr[0]-1])
