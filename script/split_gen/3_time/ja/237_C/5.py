def main():
    S = input()
    N = len(S)
    S = S + S[::-1]
    for i in range(N):
        if S[i] != S[-i-1]:
            print("No")
            return
    print("Yes")
