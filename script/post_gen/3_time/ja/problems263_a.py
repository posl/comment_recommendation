Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C, D, E = map(int, input().split())
    if A == B == C or A == B == D or A == B == E or A == C == D or A == C == E or A == D == E or B == C == D or B == C == E or B == D == E or C == D == E:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    A,B,C,D,E = map(int,input().split())
    if (A==B==C and D==E) or (A==B and C==D==E):
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    A,B,C,D,E = map(int,input().split())
    if A == B == C:
        if D == E:
            print("Yes")
        else:
            print("No")
    elif A == B == D:
        if C == E:
            print("Yes")
        else:
            print("No")
    elif A == B == E:
        if C == D:
            print("Yes")
        else:
            print("No")
    elif A == C == D:
        if B == E:
            print("Yes")
        else:
            print("No")
    elif A == C == E:
        if B == D:
            print("Yes")
        else:
            print("No")
    elif A == D == E:
        if B == C:
            print("Yes")
        else:
            print("No")
    elif B == C == D:
        if A == E:
            print("Yes")
        else:
            print("No")
    elif B == C == E:
        if A == D:
            print("Yes")
        else:
            print("No")
    elif B == D == E:
        if A == C:
            print("Yes")
        else:
            print("No")
    elif C == D == E:
        if A == B:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 4

def main():
    A,B,C,D,E = map(int,input().split())
    if A == B and B == C and D == E:
        print("Yes")
    elif A == B and B == D and C == E:
        print("Yes")
    elif A == B and B == E and C == D:
        print("Yes")
    elif A == C and C == D and B == E:
        print("Yes")
    elif A == C and C == E and B == D:
        print("Yes")
    elif A == D and D == E and B == C:
        print("Yes")
    elif B == C and C == D and A == E:
        print("Yes")
    elif B == C and C == E and A == D:
        print("Yes")
    elif B == D and D == E and A == C:
        print("Yes")
    elif C == D and D == E and A == B:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    nums = list(map(int, input().split()))
    if len(set(nums)) == 2:
        if nums.count(nums[0]) == 2 or nums.count(nums[0]) == 3:
            print("Yes")
            return
    print("No")

main()

=======
Suggestion 6

def main():
    # 入力
    A, B, C, D, E = map(int, input().split())
    # 処理
    if A == B and B == C and D == E:
        print("Yes")
    elif A == B and C == D and D == E:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    #input
    A,B,C,D,E = map(int,input().split())

    #output
    if A == B == C and D == E:
        print('Yes')
    elif A == B and C == D == E:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    #A,B,C,D,E = map(int, input().split())
    A,B,C,D,E = 1,2,1,2,1
    if A == B == C or A == B == D or A == B == E or A == C == D or A == C == E or A == D == E or B == C == D or B == C == E or B == D == E or C == D == E:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    # A,B,C,D,E = map(int,input().split())
    # print(A,B,C,D,E)
    A,B,C,D,E = 1,2,1,2,1
    #A,B,C,D,E = 12,12,11,1,2
    #A,B,C,D,E = 1,2,3,4,5
    #A,B,C,D,E = 1,1,1,1,1
    #A,B,C,D,E = 1,2,3,2,1
    #A,B,C,D,E = 1,2,3,3,2
    #A,B,C,D,E = 1,2,3,3,3
    #A,B,C,D,E = 1,2,3,2,2
    #A,B,C,D,E = 1,2,3,1,1
    #A,B,C,D,E = 1,2,3,1,2
    #A,B,C,D,E = 1,2,3,2,1
    #A,B,C,D,E = 1,2,3,1,3
    #A,B,C,D,E = 1,2,3,3,1
    #A,B,C,D,E = 1,2,3,2,3
    #A,B,C,D,E = 1,2,3,3,2
    #A,B,C,D,E = 1,2,1,2,1
    #A,B,C,D,E = 1,2,1,2,2
    #A,B,C,D,E = 1,2,1,2,3
    #A,B,C,D,E = 1,2,1,3,1
    #A,B,C,D,E = 1,2,1,3,2
    #A,B,C,D,E = 1,2,1,3,3
    #A,B,C,D,E = 1,2,2,2,1
    #A,B,C,D,E = 1,2,2,2,2
    #A,B,C,D,E = 1,2,2,2,3
    #A,B,C,D,E = 1,2,2,3,1
