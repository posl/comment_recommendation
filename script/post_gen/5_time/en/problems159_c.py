Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    L = int(input())
    print((L/3)**3 if L % 3 == 0 else ((L-1)/3)**3 if L % 3 == 1 else ((L-2)/3)**3)

=======
Suggestion 2

def main():
    l = int(input())
    print((l/3)**3 if l%3==0 else ((l-1)/3)**3 if l%3==1 else ((l-2)/3)**3)

=======
Suggestion 3

def main():
    l = int(input())
    print((l/3)**3 if l%3==0 else (l//3+1)*(l//3)*(l//3))

=======
Suggestion 4

def main():
    L = int(input())
    print((L/3)**3 if L % 3 == 0 else (L/3)**3 if L % 3 == 1 else (L//3+1)**3)

=======
Suggestion 5

def main():
    L = int(input())
    print((L/3)**3)

=======
Suggestion 6

def main():
    L = int(input())
    print(L**3/27)

=======
Suggestion 7

def main():
    L = int(input().strip())
    print((L/3)**3)
