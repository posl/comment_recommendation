def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(1, 26):
        S = S[1:] + S[0]
        if S == T:
            print("Yes")
            return
    print("No")
