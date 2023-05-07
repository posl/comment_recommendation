def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    if S == T:
        print("Yes")
        return
    if len(set(S)) == len(set(T)):
        print("Yes")
        return
    print("No")
