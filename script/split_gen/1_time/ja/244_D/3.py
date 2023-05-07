def main():
    S = input().split()
    T = input().split()
    if S == T:
        print('Yes')
    elif (S[0] == T[0] and S[1] == T[1]) or (S[0] == T[1] and S[1] == T[0]) or (S[1] == T[0] and S[2] == T[1]) or (S[1] == T[1] and S[2] == T[0]) or (S[0] == T[0] and S[2] == T[2]) or (S[0] == T[2] and S[2] == T[0]):
        print('Yes')
    else:
        print('No')
