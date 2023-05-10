Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    s = list(input().split())
    t = list(input().split())
    if s == t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

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

=======
Suggestion 5

def main():
    #data load
    S = input()
    T = input()
    #print(S)
    #print(T)
    #main
    if S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    S = input().rstrip()
    T = input().rstrip()
    if S == T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    s = input()
    t = input()
    print("Yes" if s == t else "No")

=======
Suggestion 9

def main():
    # data load
    input_data = input()
    input_data = input_data.split()
    S1 = input_data[0]
    S2 = input_data[1]
    S3 = input_data[2]
    input_data = input()
    input_data = input_data.split()
    T1 = input_data[0]
    T2 = input_data[1]
    T3 = input_data[2]

    # data check
    #print(S1)
    #print(S2)
    #print(S3)
    #print(T1)
    #print(T2)
    #print(T3)

    # count check
    cnt_r = 0
    cnt_g = 0
    cnt_b = 0
    cnt_r += S1.count("R")
    cnt_r += S2.count("R")
    cnt_r += S3.count("R")
    cnt_g += S1.count("G")
    cnt_g += S2.count("G")
    cnt_g += S3.count("G")
    cnt_b += S1.count("B")
    cnt_b += S2.count("B")
    cnt_b += S3.count("B")
    #print(cnt_r)
    #print(cnt_g)
    #print(cnt_b)

    # result
    if cnt_r == 1 and cnt_g == 1 and cnt_b == 1:
        print("Yes")
    else:
        print("No")
