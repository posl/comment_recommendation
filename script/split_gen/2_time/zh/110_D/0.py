def main():
    S = list(input())
    T = list(input())
    if len(S) != len(T):
        print("No")
        return
    if S == T:
        print("Yes")
        return
    for i in range(len(S)):
        if S[i] != T[i]:
            for j in range(i+1, len(S)):
                if S[j] == T[i]:
                    S[i], S[j] = S[j], S[i]
                    break
            else:
                print("No")
                return
    if S == T:
        print("Yes")
    else:
        print("No")
