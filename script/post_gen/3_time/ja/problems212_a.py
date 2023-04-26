Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if A > 0 and B == 0:
        print("Gold")
    elif A == 0 and B > 0:
        print("Silver")
    else:
        print("Alloy")

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if A > 0 and B > 0:
        print("Alloy")
    elif A > 0 and B == 0:
        print("Gold")
    elif A == 0 and B > 0:
        print("Silver")

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    if 0 < A and B == 0:
        print("Gold")
    elif A == 0 and 0 < B:
        print("Silver")
    else:
        print("Alloy")

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    if 0 < A and B == 0:
        print('Gold')
    elif A == 0 and 0 < B:
        print('Silver')
    else:
        print('Alloy')

main()

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    if 0 < A and B == 0:
        print('Gold')
    elif A == 0 and 0 < B:
        print('Silver')
    elif 0 < A and 0 < B:
        print('Alloy')

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    if 0 < a and b == 0:
        print("Gold")
    elif a == 0 and 0 < b:
        print("Silver")
    else:
        print("Alloy")

=======
Suggestion 7

def main():
    A, B = [int(x) for x in input().split()]
    if 0 < A and B == 0:
        print("Gold")
    elif A == 0 and 0 < B:
        print("Silver")
    elif 0 < A and 0 < B:
        print("Alloy")

=======
Suggestion 8

def main():
    A,B = map(int,input().split())
    if A == 0 and B != 0:
        print('Silver')
    elif A != 0 and B == 0:
        print('Gold')
    else:
        print('Alloy')

=======
Suggestion 9

def main():
    # A,Bを取得
    A,B = map(int, input().split())
    # 出力
    if A > 0 and B == 0:
        print("Gold")
    elif A == 0 and B > 0:
        print("Silver")
    else:
        print("Alloy")
