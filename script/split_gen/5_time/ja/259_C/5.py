def main():
    S = input()
    T = input()
    while len(S) < len(T):
        if S[-1] == T[-1]:
            if S[0] == T[0]:
                S = S[0] + S + S[1:]
            else:
                S = S + S[0]
        else:
            break
    if S == T:
        print("Yes")
    else:
        print("No")
