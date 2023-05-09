def main():
    N = int(input())
    S = input()
    R = S.count("R")
    G = S.count("G")
    B = S.count("B")
    ans = R*G*B
    for i in range(N-2):
        for j in range(i+1,N-1):
            if S[i] == S[j]:
                continue
            if S[i] == "R":
                if S[j] == "G":
                    k = "B"
                else:
                    k = "G"
            elif S[i] == "G":
                if S[j] == "R":
                    k = "B"
                else:
                    k = "R"
            elif S[i] == "B":
                if S[j] == "R":
                    k = "G"
                else:
                    k = "R"
            if j+(j-i) < N:
                if S[j+(j-i)] == k:
                    ans -= 1
    print(ans)
