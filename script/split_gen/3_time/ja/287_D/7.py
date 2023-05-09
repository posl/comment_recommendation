def main():
    S = input()
    T = input()
    N = len(S)
    M = len(T)
    for i in range(M+1):
        S_ = S[i:N-M+i]
        for j in range(M):
            if S_[j] == T[j] or S_[j] == "?" or T[j] == "?":
                if j == M-1:
                    print("Yes")
            else:
                print("No")
                break
