Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x1, x2, x3, x4, x5 = map(int, input().split())
    if x1 == 0:
        print(1)
    elif x2 == 0:
        print(2)
    elif x3 == 0:
        print(3)
    elif x4 == 0:
        print(4)
    elif x5 == 0:
        print(5)

=======
Suggestion 2

def main():
    x = list(map(int, input().split()))
    for i in range(len(x)):
        if x[i] == 0:
            print(i+1)

=======
Suggestion 3

def main():
    x = list(map(int, input().split()))
    for i in range(5):
        if x[i] == 0:
            print(i + 1)

=======
Suggestion 4

def main():
    x = list(map(int, input().split()))
    print(x.index(0) + 1)

=======
Suggestion 5

def main():
    nums = list(map(int, input().split()))
    for i in range(1, 6):
        if nums[i - 1] == 0:
            print(i)

=======
Suggestion 6

def main():
    #入力
    x_1, x_2, x_3, x_4, x_5 = map(int, input().split())

    #出力
    print(x_1.index(0)+1)

=======
Suggestion 7

def main():
    l = list(map(int, input().split()))
    print(l.index(0) + 1)
