def main():
    S = input()
    N = len(S)
    for i in range(N):
        if S[i] != S[N - i - 1]:
            print("No")
            return
    print("Yes")
    return
