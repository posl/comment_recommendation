def main():
    N, Q = map(int, input().split())
    S = input()
    l = [0] * N
    for i in range(N - 1):
        if S[i:i + 2] == "AC":
            l[i + 1] = l[i] + 1
        else:
            l[i + 1] = l[i]
    for i in range(Q):
        li, ri = map(int, input().split())
        print(l[ri - 1] - l[li - 1])
