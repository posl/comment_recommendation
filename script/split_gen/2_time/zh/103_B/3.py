def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    for i in range(len(S)):
        S = S[1:] + S[0]
        if S == T:
            print("Yes")
            return
    print("No")
    return
