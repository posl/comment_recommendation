Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, A = map(int, input().split())
    print((H + A - 1) // A)

=======
Suggestion 2

def main():
    H, A = map(int, input().split())
    print(H // A + (H % A != 0))

=======
Suggestion 3

def main():
    h,a = map(int,input().split())
    print((h-1)//a+1)
