def main():
    S = list(input())
    T = list(input())
    if len(S) + 1 < len(T):
        return print("No")
    for i in range(len(T)):
        if S[i] != T[i]:
            if S[i] == T[i + 1]:
                S.insert(i, T[i])
            else:
                return print("No")
    return print("Yes")
