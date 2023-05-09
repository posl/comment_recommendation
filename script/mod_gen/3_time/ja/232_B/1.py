def main():
    S = input()
    T = input()
    flag = False
    for i in range(len(S)):
        if S[i] == T[i]:
            flag = True
        else:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()