def main():
    S = input().split()
    T = input().split()
    if S == T:
        print("Yes")
    elif S[0] == T[0] and S[1] == T[1]:
        print("Yes")
    elif S[0] == T[0] and S[2] == T[2]:
        print("Yes")
    elif S[1] == T[1] and S[2] == T[2]:
        print("Yes")
    elif S[0] == T[1] and S[1] == T[2]:
        print("Yes")
    elif S[0] == T[2] and S[1] == T[0]:
        print("Yes")
    elif S[0] == T[1] and S[2] == T[0]:
        print("Yes")
    elif S[0] == T[2] and S[2] == T[1]:
        print("Yes")
    elif S[1] == T[0] and S[2] == T[2]:
        print("Yes")
    elif S[1] == T[2] and S[2] == T[0]:
        print("Yes")
    else:
        print("No")
main()

if __name__ == '__main__':
    main()