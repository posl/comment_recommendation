Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S1, S2, S3 = input().split()
    T1, T2, T3 = input().split()
    S = S1 + S2 + S3
    T = T1 + T2 + T3
    if S == 'RGB' and T == 'RGB':
        print('Yes')
    elif S == 'RBG' and T == 'RBG':
        print('Yes')
    elif S == 'BGR' and T == 'BGR':
        print('Yes')
    elif S == 'BRG' and T == 'BRG':
        print('Yes')
    elif S == 'GRB' and T == 'GRB':
        print('Yes')
    elif S == 'GBR' and T == 'GBR':
        print('Yes')
    else:
        print('No')
main()

=======
Suggestion 2

def main():
    S1, S2, S3 = input().split()
    T1, T2, T3 = input().split()
    if S1 == T1 and S2 == T2 and S3 == T3:
        print("Yes")
    elif S1 == T1 and S2 == T3 and S3 == T2:
        print("Yes")
    elif S1 == T2 and S2 == T1 and S3 == T3:
        print("Yes")
    elif S1 == T2 and S2 == T3 and S3 == T1:
        print("Yes")
    elif S1 == T3 and S2 == T1 and S3 == T2:
        print("Yes")
    elif S1 == T3 and S2 == T2 and S3 == T1:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 3

def main():
    S1, S2, S3 = input().split()
    T1, T2, T3 = input().split()
    S = S1+S2+S3
    T = T1+T2+T3
    if S == 'RGB' and T == 'RGB':
        print('Yes')
    elif S == 'RGB' and T == 'RBG':
        print('Yes')
    elif S == 'RBG' and T == 'RGB':
        print('Yes')
    elif S == 'RBG' and T == 'BGR':
        print('Yes')
    elif S == 'BGR' and T == 'RBG':
        print('Yes')
    elif S == 'BGR' and T == 'BRG':
        print('Yes')
    elif S == 'BRG' and T == 'BGR':
        print('Yes')
    elif S == 'BRG' and T == 'GRB':
        print('Yes')
    elif S == 'GRB' and T == 'BRG':
        print('Yes')
    elif S == 'GRB' and T == 'GBR':
        print('Yes')
    elif S == 'GBR' and T == 'GRB':
        print('Yes')
    elif S == 'GBR' and T == 'RGB':
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    S = input().split()
    T = input().split()
    if S[0] == T[0] and S[1] == T[1] and S[2] == T[2]:
        print("Yes")
    elif S[0] == T[0] and S[1] == T[2] and S[2] == T[1]:
        print("Yes")
    elif S[0] == T[1] and S[1] == T[0] and S[2] == T[2]:
        print("Yes")
    elif S[0] == T[1] and S[1] == T[2] and S[2] == T[0]:
        print("Yes")
    elif S[0] == T[2] and S[1] == T[0] and S[2] == T[1]:
        print("Yes")
    elif S[0] == T[2] and S[1] == T[1] and S[2] == T[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    S = input().split()
    T = input().split()
    if S[0] == T[0] and S[1] == T[1] and S[2] == T[2]:
        print("Yes")
    elif S[0] == T[1] and S[1] == T[2] and S[2] == T[0]:
        print("Yes")
    elif S[0] == T[2] and S[1] == T[0] and S[2] == T[1]:
        print("Yes")
    elif S[0] == T[0] and S[1] == T[2] and S[2] == T[1]:
        print("Yes")
    elif S[0] == T[1] and S[1] == T[0] and S[2] == T[2]:
        print("Yes")
    elif S[0] == T[2] and S[1] == T[1] and S[2] == T[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    S = input().split()
    T = input().split()
    if (S[0] == T[0] and S[1] == T[1] and S[2] == T[2]) or \
       (S[0] == T[0] and S[1] == T[2] and S[2] == T[1]) or \
       (S[0] == T[1] and S[1] == T[0] and S[2] == T[2]) or \
       (S[0] == T[1] and S[1] == T[2] and S[2] == T[0]) or \
       (S[0] == T[2] and S[1] == T[0] and S[2] == T[1]) or \
       (S[0] == T[2] and S[1] == T[1] and S[2] == T[0]):
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    S = input().split()
    T = input().split()
    if (S[0] == S[1] and S[1] == S[2]) or (T[0] == T[1] and T[1] == T[2]):
        print("Yes")
    elif (S[0] == S[1] and T[0] == T[1]) or (S[1] == S[2] and T[1] == T[2]) or (S[2] == S[0] and T[2] == T[0]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    s = input().split()
    t = input().split()
    if len(set(s)) == 3 and len(set(t)) == 3:
        print("Yes")
    elif len(set(s)) == 2 and len(set(t)) == 2:
        print("Yes")
    elif len(set(s)) == 1 and len(set(t)) == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    s = list(input())
    t = list(input())
    s.sort()
    t.sort()
    if s == t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    #input
    S = input().split()
    T = input().split()

    #compute

    #output
    if S == T:
        print('Yes')
    elif S[0] == T[0] and S[1] == T[1] or S[1] == T[0] and S[2] == T[1] or S[2] == T[0] and S[0] == T[1] or S[0] == T[1] and S[1] == T[0] or S[1] == T[1] and S[2] == T[0] or S[2] == T[1] and S[0] == T[0]:
        print('Yes')
    else:
        print('No')
