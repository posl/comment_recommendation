def main():
    S = input()
    T = input()
    N = len(S)
    for i in range(N):
        if S[i] != T[i]:
            print(i+1)
            return
    print(N+1)
