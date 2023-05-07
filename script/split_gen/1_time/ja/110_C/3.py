def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    for i in range(len(S)):
        if S.count(S[i]) != T.count(T[i]):
            print("No")
            return
    print("Yes")
