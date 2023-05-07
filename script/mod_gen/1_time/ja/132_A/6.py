def main():
    S = input()
    #print(S)
    if S.count(S[0]) == 2 and S.count(S[1]) == 2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()