def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    S_max = S[0]
    S_len = 1
    S_max_len = 1
    for i in range(1, N):
        if S[i] == S[i-1]:
            S_len += 1
            if S_len > S_max_len:
                S_max_len = S_len
                S_max = S[i]
        else:
            S_len = 1
    print(S_max)
