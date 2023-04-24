Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c, d = map(int, input().split())
    print(max(a*c, a*d, b*c, b*d))

=======
Suggestion 2

def main():
    a,b,c,d = map(int,input().split())
    ans = max(a*c,a*d,b*c,b*d)
    print(ans)

=======
Suggestion 3

def main():
    #input
    a, b, c, d = map(int, input().split())
    #output
    print(max(a*c, a*d, b*c, b*d))

=======
Suggestion 4

def main():
    a,b,c,d = map(int,input().split())
    print(max(a*d,b*d,a*c,b*c))

=======
Suggestion 5

def main():
    #入力
    a,b,c,d = map(int,input().split())
    #処理
    if a >= 0 and c >= 0:
        print(a*d)
    elif a >= 0 and c < 0:
        if d >= 0:
            print(a*d)
        else:
            print(a*c)
    elif a < 0 and c >= 0:
        if b >= 0:
            print(b*d)
        else:
            print(a*d)
    elif a < 0 and c < 0:
        if b >= 0:
            if d >= 0:
                print(max(a*d,b*c))
            else:
                print(max(a*c,b*c))
        else:
            print(max(a*c,b*d))
