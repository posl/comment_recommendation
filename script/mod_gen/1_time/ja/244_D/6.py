def main():
    S = list(input().split())
    T = list(input().split())
    if S == T:
        print("Yes")
        return
    if S[0] == S[1] and S[1] == S[2]:
        print("No")
        return
    if S[0] == S[1] or S[1] == S[2] or S[2] == S[0]:
        print("Yes")
        return
    print("Yes")

if __name__ == '__main__':
    main()