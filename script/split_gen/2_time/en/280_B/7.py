def main():
    N = int(input())
    S = list(map(int, input().split()))
    # A_1 = S_1
    A = [S[0]]
    # A_i = S_i - S_i-1
    for i in range(1, N):
        A.append(S[i] - S[i-1])
    print(*A)
