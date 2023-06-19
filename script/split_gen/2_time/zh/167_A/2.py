def main():
    S = input()
    T = input()
    if len(S) == len(T) - 1:
        if S == T[:-1]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
