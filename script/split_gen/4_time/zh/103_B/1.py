def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
    else:
        for i in range(len(S)):
            if S[i:] + S[:i] == T:
                print("Yes")
                break
        else:
            print("No")
