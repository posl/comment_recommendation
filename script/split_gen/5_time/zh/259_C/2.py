def main():
    S = input()
    T = input()
    if len(S) + 1 == len(T):
        if S == T[:-1]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
