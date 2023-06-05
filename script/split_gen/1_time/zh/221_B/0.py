def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            if S[i] == T[j] and S[j] == T[i]:
                print("Yes")
                return
    print("No")
