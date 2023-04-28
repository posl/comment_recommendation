Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, A = map(int, input().split())
    count = 0
    while H > 0:
        H -= A
        count += 1
    print(count)

=======
Suggestion 2

def main():
    H, A = map(int, input().split())

    if H % A == 0:
        print(H // A)
    else:
        print(H // A + 1)

=======
Suggestion 3

def main():
    H, A = map(int, input().split())
    ans = H // A
    if H % A != 0:
        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    H,A = map(int,input().split())
    count = 0
    while True:
        count += 1
        H -= A
        if H <= 0:
            break
    print(count)

=======
Suggestion 5

def main():
    h,a = map(int,input().split())
    if h%a==0:
        print(h//a)
    else:
        print(h//a+1)

=======
Suggestion 6

def main():
    h, a = map(int, input().split())
    print((h + a - 1) // a)

=======
Suggestion 7

def main():
    h, a = map(int, input().split())
    print((h-1)//a + 1)

=======
Suggestion 8

def calc(h,a):
    if h % a == 0:
        return h // a
    else:
        return h // a + 1

=======
Suggestion 9

def main():
    h,a = [int(x) for x in input().split()]
    print((h-1)//a + 1)
