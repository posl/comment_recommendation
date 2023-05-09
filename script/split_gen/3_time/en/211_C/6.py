def main():
    S = input()
    MOD = 10**9 + 7
    N = len(S)
    C = [0] * 8
    for i in range(N):
        if S[i] == "c":
            C[0] += 1
        elif S[i] == "h":
            C[1] += C[0]
        elif S[i] == "o":
            C[2] += C[1]
        elif S[i] == "k":
            C[3] += C[2]
        elif S[i] == "u":
            C[4] += C[3]
        elif S[i] == "d":
            C[5] += C[4]
        elif S[i] == "a":
            C[6] += C[5]
        elif S[i] == "i":
            C[7] += C[6]
    print(C[7] % MOD)
