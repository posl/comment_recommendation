def main():
    S = input()
    T = input()
    if len(S) > len(T):
        print("No")
        return
    if S == T:
        print("Yes")
        return
    for i in range(len(S)):
        if S[i] == T[i]:
            continue
        if S[i] != T[i+1]:
            print("No")
            return
        if S[i+1] != T[i+2]:
            print("No")
            return
    print("Yes")
