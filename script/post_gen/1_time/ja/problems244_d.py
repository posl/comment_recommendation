Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input().split()
    T = input().split()
    if (S[0] == T[0] and S[1] == T[1] and S[2] == T[2]) or (S[0] == T[0] and S[2] == T[1] and S[1] == T[2]) or (S[1] == T[0] and S[0] == T[1] and S[2] == T[2]) or (S[1] == T[0] and S[2] == T[1] and S[0] == T[2]) or (S[2] == T[0] and S[0] == T[1] and S[1] == T[2]) or (S[2] == T[0] and S[1] == T[1] and S[0] == T[2]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = input().split()
    T = input().split()
    S.sort()
    T.sort()
    if S == T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

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

=======
Suggestion 4

def main():
    S = input().split()
    T = input().split()
    if S == T:
        print('Yes')
    elif (S[0] == T[0] and S[1] == T[1]) or (S[0] == T[1] and S[1] == T[0]) or (S[1] == T[0] and S[2] == T[1]) or (S[1] == T[1] and S[2] == T[0]) or (S[0] == T[0] and S[2] == T[2]) or (S[0] == T[2] and S[2] == T[0]):
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    S = input().split()
    T = input().split()
    for i in range(3):
        for j in range(i+1,3):
            if S[i] == T[i] and S[j] == T[j]:
                print("Yes")
                return
    print("No")

=======
Suggestion 6

def main():
    S = list(input().split())
    T = list(input().split())
    if S == T:
        print('Yes')
        return
    if S[0] == S[1] and S[1] == S[2]:
        print('No')
        return
    if T[0] == T[1] and T[1] == T[2]:
        print('No')
        return
    print('Yes')
    return

main()

=======
Suggestion 7

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

=======
Suggestion 8

def main():
    S = input().split()
    T = input().split()
    if S == T:
        print('Yes')
    elif S[0] == S[1] and S[0] == S[2]:
        print('No')
    elif S[0] == S[1] and T[0] == T[1]:
        print('Yes')
    elif S[1] == S[2] and T[1] == T[2]:
        print('Yes')
    elif S[0] == S[2] and T[0] == T[2]:
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 9

def main():
    S = input().split()
    T = input().split()
    if S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    S = input().split()
    T = input().split()
    if S == T:
        print('Yes')
        return
    if S == T[::-1]:
        print('Yes')
        return
    if S[0] == S[1] and S[1] == S[2] and S[2] == T[0] and T[0] == T[1] and T[1] == T[2]:
        print('Yes')
        return
    print('No')
    return
