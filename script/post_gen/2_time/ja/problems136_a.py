Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    if A - B >= C:
        print(C)
    else:
        print(A - B)

=======
Suggestion 2

def main():
    A, B, C = map(int, input().split())
    if A - B < C:
        print(A - B)
    else:
        print(C)

=======
Suggestion 3

def main():
    A, B, C = map(int, input().split())
    if B + C <= A:
        print(0)
    else:
        print(B + C - A)

=======
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    print(C - (A - B) if A - B < C else 0)

main()

=======
Suggestion 5

def main():
    A, B, C = map(int, input().split())
    if B+C >= A:
        print(B+C-A)
    else:
        print(0)

=======
Suggestion 6

def main():
    A, B, C = map(int, input().split())
    if A-B >= C:
        print(C)
    else:
        print(C-(A-B))

=======
Suggestion 7

def main():
    a, b, c = map(int, input().split())
    print(max(c-(a-b), 0))

=======
Suggestion 8

def main():
    A, B, C = map(int, input().split())
    print(max(0, min(C, B + C - A)))

=======
Suggestion 9

def main():
    # A,B,C = 6,4,3
    A,B,C = map(int,input().split())
    if B + C <= A:
        print(C)
    else:
        print(C - (A - B))
