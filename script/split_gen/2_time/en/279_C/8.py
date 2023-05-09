def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    for p in permutations(range(W), W):
        S_ = ["".join(S[i][p[j]] for j in range(W)) for i in range(H)]
        if S_ == T:
            print("Yes")
            return
    print("No")
