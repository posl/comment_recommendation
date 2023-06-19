def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(1, len(S)):
        if S[i:] + S[:i] == T:
            print("Yes")
            return
    print("No")
    return
main()
