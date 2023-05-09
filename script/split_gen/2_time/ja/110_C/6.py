def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    for i in range(len(S)):
        if S[i] == T[i]:
            continue
        elif S[i] in T and T[i] in S:
            continue
        else:
            print("No")
            return
    print("Yes")
    return
