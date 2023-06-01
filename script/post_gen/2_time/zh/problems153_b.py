Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_input():
    return map(int, input().split())

=======
Suggestion 2

def main():
    H,A=map(int,input().split())
    ans=H//A
    if H%A!=0:
        ans+=1
    print(ans)

=======
Suggestion 3

def main():
    H,A = map(int,input().split())
    count = 0
    while H > 0:
        H -= A
        count += 1
    print(count)

=======
Suggestion 4

def main():
    H, A = map(int, input().split())
    if H % A == 0:
        print(H // A)
    else:
        print(H // A + 1)

=======
Suggestion 5

def main():
    h, a = map(int, input().split())
    print((h+a-1)//a)

=======
Suggestion 6

def main():
    H, A = map(int, input().split())
    print((H + A - 1) // A)

=======
Suggestion 7

def main():
    h,a = map(int,input().split())
    i = 0
    while h > 0:
        h -= a
        i += 1
    print(i)

=======
Suggestion 8

def main():
    H, A = map(int, input().split())
    print(H // A + (1 if H % A else 0))
