def main():
    S = input().split()
    T = input().split()
    if (S[0] == S[1] and S[1] == S[2]) or (T[0] == T[1] and T[1] == T[2]):
        print("Yes")
    elif (S[0] == S[1] and T[0] == T[1]) or (S[1] == S[2] and T[1] == T[2]) or (S[2] == S[0] and T[2] == T[0]):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()