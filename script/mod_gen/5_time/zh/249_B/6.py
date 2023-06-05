def main():
    S = input()
    if S.islower() == True:
        print("No")
        return
    if S.isupper() == True:
        print("No")
        return
    if len(S) % 2 == 1:
        print("No")
        return
    for i in range(0,len(S),2):
        if S[i].isupper() == False:
            print("No")
            return
    for i in range(1,len(S),2):
        if S[i].islower() == False:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()