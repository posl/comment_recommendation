Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, A = map(int, input().split())
    if H % A == 0:
        print(H // A)
    else:
        print(H // A + 1)

=======
Suggestion 2

def main():
    H, A = map(int, input().split())
    if H % A == 0:
        print(int(H / A))
    else:
        print(int(H / A) + 1)

=======
Suggestion 3

def solve():
    H, A = map(int, input().split())
    print((H + A - 1) // A)
    return 0

=======
Suggestion 4

def main():
    H,A = map(int,input().split())
    res = H//A
    if H%A != 0:
        res += 1
    print(res)

=======
Suggestion 5

def main():
    h,a = map(int,input().split())
    if h%a == 0:
        print(h//a)
    else:
        print(h//a+1)

=======
Suggestion 6

def main():
    h,a = map(int,input().split())
    if h % a == 0:
        print(int(h/a))
    else:
        print(int(h/a)+1)

=======
Suggestion 7

def main():
    H,A = map(int,input().split())
    print((H+A-1)//A)

=======
Suggestion 8

def main():
    h,a = map(int,input().split())
    if h%a == 0:
        print(h//a)
    else:
        print(h//a+1)

main()

=======
Suggestion 9

def get_input():
    input_str = input().split(' ')
    return int(input_str[0]), int(input_str[1])
