Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    h, a = map(int, input().split())
    if h % a == 0:
        print(h // a)
    else:
        print(h // a + 1)

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
    ans = 0
    while H > 0:
        H -= A
        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    H, A = map(int, input().split())
    result = 0
    while H > 0:
        result += 1
        H -= A
    print(result)

=======
Suggestion 5

def main():
    H, A = map(int, input().split())
    print((H + A - 1) // A)

=======
Suggestion 6

def main():
    H, A = map(int, input().split())
    print(H//A if H%A==0 else H//A+1)
