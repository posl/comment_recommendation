Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = list(map(int, input().split()))
    for i in range(5):
        if x[i] == 0:
            print(i+1)

=======
Suggestion 2

def main():
    x = list(map(int, input().split()))
    for i in range(1, 6):
        if x[i - 1] == 0:
            print(i)
            break

=======
Suggestion 3

def main():
    x = list(map(int, input().split()))
    print(x.index(0) + 1)

=======
Suggestion 4

def main():
    x = input().split()
    for i in range(5):
        if x[i] == '0':
            print(i+1)

=======
Suggestion 5

def main():
    x_list = list(map(int, input().split()))
    for idx, x in enumerate(x_list):
        if x == 0:
            print(idx+1)
            break

=======
Suggestion 6

def main():
    #入力
    x1,x2,x3,x4,x5 = map(int,input().split())
    #出力
    print(x1.index(0)+1)
