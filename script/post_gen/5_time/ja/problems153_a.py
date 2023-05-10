Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, A = map(int, input().split())
    if H % A == 0:
        print(H//A)
    else:
        print(H//A + 1)

main()

=======
Suggestion 2

def main():
    H, A = map(int, input().split())
    print((H+A-1)//A)

=======
Suggestion 3

def main():
    h, a = map(int, input().split())
    print((h + a - 1) // a)

=======
Suggestion 4

def main():
    h,a = map(int,input().split())
    cnt = 0
    while h > 0:
        h -= a
        cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    H, A = map(int, input().split())
    print(H//A if H%A==0 else H//A+1)

=======
Suggestion 6

def main():
    h, a = map(int, input().split())
    print((h-1)//a+1)

=======
Suggestion 7

def main():
    H, A = map(int, input().split())
    count = 0
    while H > 0:
        H -= A
        count += 1
    print(count)

=======
Suggestion 8

def main():
    H, A = map(int, input().split())
    if H % A == 0:
        print(int(H / A))
    else:
        print(int(H / A) + 1)

=======
Suggestion 9

def main():
    H, A = map(int, input().split())
    if H % A == 0:
        print(H // A)
    else:
        print(H // A + 1)
