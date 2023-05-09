def main():
    S = input()
    if S[0] == S[0].lower():
        print("No")
        exit(0)
    for i in range(1,len(S)):
        if i % 2 == 0:
            if S[i] == S[i].lower():
                print("No")
                exit(0)
        else:
            if S[i] == S[i].upper():
                print("No")
                exit(0)
    print("Yes")
main()
