Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s,t,x = map(int,input().split())
    if s < t:
        if s <= x and x < t:
            print("Yes")
        else:
            print("No")
    else:
        if s <= x or x < t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def main():
    S, T, X = map(int, input().split())
    if S < T:
        if S <= X and X < T:
            print('Yes')
        else:
            print('No')
    elif S > T:
        if S <= X or X < T:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 3

def main():
    S, T, X = map(int, input().split())
    if X+0.5 >= S and X+0.5 < T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    S, T, X = map(int, input().split())
    if S <= X and X < T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    S, T, X = map(int, input().split())
    if (X >= S and X < T) or (S > T and (X >= S or X < T)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    S, T, X = map(int, input().split())
    if S <= X and X < T:
        print("Yes")
    elif S <= X + 24 and X + 24 < T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    s, t, x = map(int, input().split())
    if s <= x < t:
        print("Yes")
    elif s > t and s <= x:
        print("Yes")
    elif s > t and x < t:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    S, T, X = map(int, input().split())
    if S <= X and X < T:
        print("Yes")
    elif S < X+1 and X+1 <= T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    S, T, X = map(int, input().split())
    if S <= X and X < T:
        print("Yes")
    elif S == T:
        print("No")
    else:
        if S > T:
            if X >= S or X < T:
                print("Yes")
            else:
                print("No")
        else:
            print("No")

=======
Suggestion 10

def main():
    S, T, X = map(int, input().split())

    # 12:30 = 30分
    # 電気がついている時間を計算
    if S > T:
        t = 24 - S + T
    else:
        t = T - S

    # 12:30 に電気がついているかどうか
    if X + 0.5 >= S and X + 0.5 < T:
        print("Yes")
    else:
        print("No")
