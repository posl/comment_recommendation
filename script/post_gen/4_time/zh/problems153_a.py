Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, A = map(int, input().split())
    print((H + A - 1) // A)

=======
Suggestion 2

def main():
    h,a = map(int,input().split())
    if h%a==0:
        print(int(h/a))
    else:
        print(int(h/a)+1)

=======
Suggestion 3

def attack_count(h, a):
    count = 0
    while h > 0:
        h = h - a
        count = count + 1
    return count

=======
Suggestion 4

def problems153_a():
    h, a = map(int, input().split())
    print((h-1)//a + 1)

=======
Suggestion 5

def main():
    H, A = map(int, input().split())
    print(-(-H//A))

=======
Suggestion 6

def main():
    h,a = map(int,input().split())
    count = 0
    while h > 0:
        h = h - a
        count += 1
    print(count)

=======
Suggestion 7

def main():
    h,a = map(int, input().split())
    print((h+a-1)//a)

=======
Suggestion 8

def main():
    H, A = map(int, input().split())
    print(H//A + (H%A!=0))

=======
Suggestion 9

def problems153_a():
    h, a = map(int, input().split())
    if h % a == 0:
        print(h // a)
    else:
        print(h // a + 1)


problems153_a()

=======
Suggestion 10

def main():
    import sys
    h,a = map(int, sys.stdin.readline().split())
    print((h-1)//a+1)
