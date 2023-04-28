Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, S, D = map(int, input().split())
    for i in range(N):
        X, Y = map(int, input().split())
        if X < S and Y > D:
            print("Yes")
            return
    print("No")

=======
Suggestion 2

def solve():
    N, S, D = map(int, input().split())
    for i in range(N):
        X, Y = map(int, input().split())
        if X < S and Y > D:
            print('Yes')
            return
    print('No')

=======
Suggestion 3

def solve():
    N, S, D = map(int, input().split())
    for i in range(N):
        X, Y = map(int, input().split())
        if X < S and Y > D:
            return "Yes"
    return "No"

print(solve())

=======
Suggestion 4

def main():
    n, s, d = map(int, input().split())
    spells = [tuple(map(int, input().split())) for _ in range(n)]
    for x, y in spells:
        if x < s and y > d:
            print('Yes')
            break
    else:
        print('No')

=======
Suggestion 5

def main():
    n, s, d = map(int, input().split())
    xy = [list(map(int, input().split())) for i in range(n)]
    for i in range(n):
        if xy[i][0] < s and xy[i][1] > d:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 6

def main():
    n,s,d = map(int,input().split())
    x = []
    y = []
    for i in range(n):
        x_i,y_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
    for i in range(n):
        if x[i] < s and y[i] > d:
            print('Yes')
            return
    print('No')

=======
Suggestion 7

def main():
    N, S, D = map(int, input().split())
    spells = []
    for _ in range(N):
        X, Y = map(int, input().split())
        spells.append((X, Y))

    for spell in spells:
        if spell[0] < S and spell[1] > D:
            print("Yes")
            return

    print("No")

=======
Suggestion 8

def main():
    n,s,d = map(int, input().split())
    spells = [list(map(int, input().split())) for _ in range(n)]

    for spell in spells:
        if spell[0] < s and spell[1] > d:
            print('Yes')
            return
    print('No')

=======
Suggestion 9

def main():
    n,s,d = map(int,input().split())
    spells = []
    for i in range(n):
        x,y = map(int,input().split())
        spells.append([x,y])
    for i in range(n):
        if spells[i][0]<s and spells[i][1]>d:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 10

def main():
    # Get input here
    N, S, D = map(int, input().strip().split())
    spells = [tuple(map(int, input().strip().split())) for _ in range(N)]

    # Calculate result here
    result = 'No'
    for x, y in spells:
        if x < S and y > D:
            result = 'Yes'
            break

    # Print result here
    print(result)

main()
