def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        for i in range(len(S)):
            if S[i] != T[i]:
                if S[i+1:] == T[i+1:]:
                    print("Yes")
                    break
                else:
                    print("No")
                    break
