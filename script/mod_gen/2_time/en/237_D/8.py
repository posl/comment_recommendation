def main():
    N = int(input())
    S = input()
    # A = [0]
    # for i in range(N):
    #     if S[i] == "L":
    #         A.insert(0, i+1)
    #     else:
    #         A.append(i+1)
    # print(*A)
    # A = [0]
    # for i in range(N):
    #     if S[i] == "L":
    #         A.insert(0, i+1)
    #     else:
    #         A.append(i+1)
    # print(*A)
    A = [0]
    for i in range(N):
        if S[i] == "L":
            A.insert(0, i+1)
        else:
            A.append(i+1)
    print(*A)
main()
The first two samples are correct. The third sample is wrong.
The third sample’s answer is “7 6 5 4 3 2 1 0 0”. The correct answer is “7 6 5 4 3 2 1 0”.
I don’t know why the third sample is wrong. I can’t find the mistake.
I’m sorry for my poor English.
Thank you for your help.
I think the problem is in your print statement. You are printing A, which is the list. You need to print the elements of A.
You can use the * operator to print the elements of A separated by spaces.

if __name__ == '__main__':
    main()