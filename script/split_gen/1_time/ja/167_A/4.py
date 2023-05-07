def main():
    S = input()
    T = input()
    if S == T[:len(S)] and S != T:
        print("Yes")
    else:
        print("No")
