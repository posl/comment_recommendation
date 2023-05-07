def main():
    S = input().split()
    T = input().split()
    if (S[0] == T[0] and S[1] == T[1] and S[2] == T[2]) or (S[0] == T[0] and S[2] == T[1] and S[1] == T[2]) or (S[1] == T[0] and S[0] == T[1] and S[2] == T[2]) or (S[1] == T[0] and S[2] == T[1] and S[0] == T[2]) or (S[2] == T[0] and S[0] == T[1] and S[1] == T[2]) or (S[2] == T[0] and S[1] == T[1] and S[0] == T[2]):
        print("Yes")
    else:
        print("No")
