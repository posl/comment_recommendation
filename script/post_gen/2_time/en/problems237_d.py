Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(N):
        if S[i] == 'L':
            A.insert(0, i+1)
        else:
            A.append(i+1)
    print(' '.join(map(str, A)))

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(N):
        if S[i] == 'L':
            A.insert(0, i+1)
        else:
            A.append(i+1)
    print(*A)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(N):
        if S[i] == "L":
            A.insert(0, i+1)
        else:
            A.append(i+1)
    print(*A)

main()

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(N):
        if S[i] == 'R':
            A.append(i+1)
        else:
            A.insert(0,i+1)
    print(*A)

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(n):
        if s[i] == 'L':
            a.insert(0, i+1)
        else:
            a.append(i+1)
    print(*a)

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(N):
        if S[i] == "L":
            A.insert(0,i+1)
        else:
            A.append(i+1)
    print(*A)

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    ans = [0]
    for i in range(n):
        if s[i] == "L":
            ans.insert(0,i+1)
        else:
            ans.append(i+1)
    print(*ans)

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    arr = [0]
    for i in range(n):
        if s[i] == 'L':
            arr.insert(0,i+1)
        else:
            arr.append(i+1)
    print(*arr)

main()

=======
Suggestion 9

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
