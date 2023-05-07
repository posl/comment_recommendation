def main():
    S = input()
    if len(S) == 1:
        print("Yes")
        exit()
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i].isupper():
                print("No")
                exit()
        else:
            if S[i].islower():
                print("No")
                exit()
    print("Yes")
