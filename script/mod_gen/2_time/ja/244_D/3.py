def main():
    S = input().split()
    T = input().split()
    if S == T:
        print("Yes")
    elif S[0] == S[1] == S[2] or T[0] == T[1] == T[2]:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()