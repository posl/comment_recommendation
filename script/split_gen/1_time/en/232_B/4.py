def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        for i in range(1, 26):
            if S[-i:] + S[:-i] == T:
                print("Yes")
                return
        print("No")
