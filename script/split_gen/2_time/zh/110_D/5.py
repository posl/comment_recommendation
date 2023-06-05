def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    if S == T:
        print("Yes")
        return
    S = list(S)
    T = list(T)
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            S[i], S[j] = S[j], S[i]
            if S == T:
                print("Yes")
                return
            S[i], S[j] = S[j], S[i]
    print("No")
