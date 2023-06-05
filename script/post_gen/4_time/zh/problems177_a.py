Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    D,T,S = map(int, input().split())
    if T*S >= D:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    input_str = input()
    input_list = input_str.split()
    D = int(input_list[0])
    T = int(input_list[1])
    S = int(input_list[2])
    if D % S == 0:
        if D / S <= T:
            print('Yes')
        else:
            print('No')
    else:
        if D / S + 1 <= T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 3

def main():
    d, t, s = map(int, input().split(' '))
    if d/s <= t:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    D, T, S = map(int, input().split())
    if D <= T * S:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def check_time(d, t, s):
    if d / s <= t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    D, T, S = map(int, input().split())
    if D / S <= T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    d,t,s = map(int, input().split())
    if d/s <= t:
        print("Yes")
    else:
        print("No")
