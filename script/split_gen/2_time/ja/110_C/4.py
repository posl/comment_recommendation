def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    if sorted(S) != sorted(T):
        print("No")
        return
    print("Yes")
