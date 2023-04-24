Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        if D[i][0] == D[i][1]:
            cnt += 1
        else:
            cnt = 0
        if cnt == 3:
            print("Yes")
            return
    print("No")

=======
Suggestion 2

def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N-2):
        if D[i][0] == D[i][1] == D[i+1][0] == D[i+1][1] == D[i+2][0] == D[i+2][1]:
            print('Yes')
            return
    print('No')

main()

Problem Statement

Tak performed the following action N times: rolling two dice.

The result of the i-th roll is D_{i,1} and D_{i,2}.

Check if doublets occurred at least three times in a row.

Specifically, check if there exists at lease one i such that D_{i,1}=D_{i,2}, D_{i+1,1}=D_{i+1,2} and D_{i+2,1}=D_{i+2,2} hold.

Constraints

3 ≦ N ≦ 100

1≦ D_{i,j} ≦ 6

All values in input are integers.

Input

Input is given from Standard Input in the following format:

N
D_{1,1} D_{1,2}
.
.
.
D_{N,1} D_{N,2}

Output

Print Yes if doublets occurred at least three times in a row. Print No otherwise.

Sample Input 1

5
1 2
6 6
4 4
3 3
3 2

Sample Output 1

Yes

From the second roll to the fourth roll, three doublets occurred in a row.

Sample Input 2

5
1 1
2 2
3 4
5 5
6 6

Sample Output 2

No

Sample Input 3

6
1 1
2 2
3 3
4 4
5 5
6 6

Sample Output 3

Yes

Problem Statement

Tak and Aok are playing a game.

The game is played on a rectangular grid with H rows and W columns.

Initially, Tak is in the upper-left cell, and Aok is in the lower-right cell.

Tak and Aok take turns to move.

Tak moves first.

In one move, a player can go to one of the four neighboring cells

=======
Suggestion 3

def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N - 2):
        if D[i][0] == D[i][1] == D[i + 1][0] == D[i + 1][1] == D[i + 2][0] == D[i + 2][1]:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 4

def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N - 2):
        if D[i][0] == D[i][1] == D[i + 1][0] == D[i + 1][1] == D[i + 2][0] == D[i + 2][1]:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 5

def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N - 2):
        if D[i][0] == D[i][1] == D[i + 1][0] == D[i + 1][1] == D[i + 2][0] == D[i + 2][1]:
            print('Yes')
            return
    print('No')
    return

=======
Suggestion 6

def main():
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n-2):
        if d[i][0] == d[i][1] == d[i+1][0] == d[i+1][1] == d[i+2][0] == d[i+2][1]:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 7

def main():
    n = int(input())
    d = []
    for i in range(n):
        d.append(list(map(int, input().split())))
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 8

def main():
    n = int(input())
    d = [list(map(int, input().split())) for i in range(n)]
    for i in range(n-2):
        if d[i][0] == d[i][1] == d[i+1][0] == d[i+1][1] == d[i+2][0] == d[i+2][1]:
            print("Yes")
            return
    print("No")

=======
Suggestion 9

def main():
    N = int(input())
    D = [list(map(int,input().split())) for _ in range(N)]
    ans = 'No'
    for i in range(N-2):
        if D[i][0]==D[i][1] and D[i+1][0]==D[i+1][1] and D[i+2][0]==D[i+2][1]:
            ans = 'Yes'
            break
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
            ans = 1
            break
    if ans == 1:
        print("Yes")
    else:
        print("No")
