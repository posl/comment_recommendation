def main():
    N, Q = map(int, input().split())
    S = input()
    count = [0] * (N + 1)
    for i in range(N):
        count[i + 1] = count[i]
        if S[i] == 'A' and S[i + 1] == 'C':
            count[i + 1] += 1
    for i in range(Q):
        l, r = map(int, input().split())
        print(count[r - 1] - count[l - 1])
