def main():
    N = int(input())
    S = [int(i) for i in input().split()]
    T = [int(i) for i in input().split()]
    res = [0 for i in range(N)]
    res[0] = T[0]
    for i in range(1, N):
        if res[i-1] + S[i-1] < T[i]:
            res[i] = T[i]
        else:
            res[i] = res[i-1] + S[i-1]
    for i in range(N):
        print(res[i])
