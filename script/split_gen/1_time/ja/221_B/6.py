def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    S = list(S)
    T = list(T)
    for i in range(len(S) - 1):
        S[i], S[i + 1] = S[i + 1], S[i]
        if S == T:
            print("Yes")
            return
        S[i], S[i + 1] = S[i + 1], S[i]
    print("No")
