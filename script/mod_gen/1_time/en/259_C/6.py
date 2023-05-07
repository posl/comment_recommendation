def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    if len(S) == 1:
        print("No")
        return
    if len(S) == 2:
        if S[0] == T[0] or S[1] == T[1]:
            print("Yes")
        else:
            print("No")
        return
    if S[0] == T[0] and S[-1] == T[-1]:
        print("Yes")
    elif S[0] == T[0]:
        print("Yes")
    elif S[-1] == T[-1]:
        print("Yes")
    else:
        print("No")
main()
I got WA and I don't know why. I think I have covered all the cases.
Can someone please help me?
Thanks in advance.
I am new to python and I am trying to write a program that will take a list of numbers and find the max and min of the list. I have the code below but when I run it, it says that the input is invalid. I don't know what I am doing wrong. Any help would be appreciated.

if __name__ == '__main__':
    main()