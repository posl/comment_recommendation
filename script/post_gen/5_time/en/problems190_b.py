Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, s, d = map(int, input().split())
    for i in range(n):
        x, y = map(int, input().split())
        if x < s and y > d:
            print("Yes")
            return
    print("No")

=======
Suggestion 2

def main():
    n, s, d = map(int, input().split())
    for i in range(n):
        x, y = map(int, input().split())
        if x < s and y > d:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 3

def main():
    n, s, d = map(int, input().split())
    for _ in range(n):
        x, y = map(int, input().split())
        if x < s and y > d:
            print("Yes")
            return
    print("No")

=======
Suggestion 4

def main():
    N, S, D = map(int, input().split())
    for i in range(N):
        X, Y = map(int, input().split())
        if X < S and Y > D:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 5

def main():
    N, S, D = map(int, input().split())
    for i in range(N):
        X, Y = map(int, input().split())
        if X < S and Y > D:
            print('Yes')
            return
    print('No')

=======
Suggestion 6

def solve():
    n, s, d = map(int, input().split())
    for _ in range(n):
        x, y = map(int, input().split())
        if x < s and y > d:
            return True
    return False

print('Yes' if solve() else 'No')

=======
Suggestion 7

def main():
    n, s, d = map(int, input().split())
    spells = [list(map(int, input().split())) for _ in range(n)]
    for x, y in spells:
        if x < s and y > d:
            print("Yes")
            return
    print("No")

=======
Suggestion 8

def main():
    n, s, d = map(int, input().split())
    spells = []
    for i in range(n):
        spells.append(list(map(int, input().split())))
    for i in range(n):
        if spells[i][0] < s and spells[i][1] > d:
            print("Yes")
            break
        else:
            print("No")
            break

=======
Suggestion 9

def main():
    N, S, D = map(int, input().split())
    spell = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        if spell[i][0] < S and spell[i][1] > D:
            print('Yes')
            return
    print('No')
    return

=======
Suggestion 10

def main():
    n,s,d = map(int, input().split())
    spells = [list(map(int, input().split())) for _ in range(n)]
    print("Yes" if any([spell[0] < s and spell[1] > d for spell in spells]) else "No")
