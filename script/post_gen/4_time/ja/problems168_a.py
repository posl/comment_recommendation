Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    if n % 10 in [2, 4, 5, 7, 9]:
        print("hon")
    elif n % 10 in [0, 1, 6, 8]:
        print("pon")
    else:
        print("bon")

=======
Suggestion 2

def main():
    N = int(input())

    if N % 10 == 2 or N % 10 == 4 or N % 10 == 5 or N % 10 == 7 or N % 10 == 9:
        print("hon")
    elif N % 10 == 0 or N % 10 == 1 or N % 10 == 6 or N % 10 == 8:
        print("pon")
    elif N % 10 == 3:
        print("bon")

main()

=======
Suggestion 3

def main():
    N = int(input())
    if N % 10 in [2, 4, 5, 7, 9]:
        print('hon')
    elif N % 10 in [0, 1, 6, 8]:
        print('pon')
    else:
        print('bon')

=======
Suggestion 4

def solve():
    n = int(input())
    if n % 10 in [2, 4, 5, 7, 9]:
        print("hon")
    elif n % 10 in [0, 1, 6, 8]:
        print("pon")
    else:
        print("bon")

=======
Suggestion 5

def main():
    n = int(input())
    hon = [2, 4, 5, 7, 9]
    pon = [0, 1, 6, 8]
    bon = [3]
    if n % 10 in hon:
        print("hon")
    elif n % 10 in pon:
        print("pon")
    else:
        print("bon")

=======
Suggestion 6

def main():
    n = int(input())
    if (n%10 == 2) or (n%10 == 4) or (n%10 == 5) or (n%10 == 7) or (n%10 == 9):
        print("hon")
    elif (n%10 == 0) or (n%10 == 1) or (n%10 == 6) or (n%10 == 8):
        print("pon")
    else:
        print("bon")

=======
Suggestion 7

def main():
    N = int(input())
    N = N % 10
    if N in [2, 4, 5, 7, 9]:
        print("hon")
    elif N in [0, 1, 6, 8]:
        print("pon")
    else:
        print("bon")

=======
Suggestion 8

def main():
    N = int(input())
    last_digit = N % 10
    if last_digit == 2 or last_digit == 4 or last_digit == 5 or last_digit == 7 or last_digit == 9:
        print("hon")
    elif last_digit == 0 or last_digit == 1 or last_digit == 6 or last_digit == 8:
        print("pon")
    else:
        print("bon")

=======
Suggestion 9

def solve():
    # === 数値の入力 ===
    #n = int(input())
    n = 183
    # === 行列の入力 ===
    #a = list(map(int, input().split()))
    #a = [1, 2, 3, 4, 5]
    # === 行列の入力 ===
    #a = [input() for _ in range(3)]
    #a = ['1', '2', '3']
    # === 行列の入力 ===
    #a = [list(map(int, input().split())) for _ in range(3)]
    #a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # === 行列の入力 ===
    #a = [list(input()) for _ in range(h)]
    #a = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    # === 行列の入力 ===
    #a = [list(input().split()) for _ in range(h)]
    #a = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    if n % 10 in [2, 4, 5, 7, 9]:
        print('hon')
    elif n % 10 in [0, 1, 6, 8]:
        print('pon')
    else:
        print('bon')
