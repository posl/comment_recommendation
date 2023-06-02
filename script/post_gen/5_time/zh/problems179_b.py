Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    D = []
    for i in range(N):
        D.append(list(map(int, input().split())))
    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 2

def check_twin_dice(n, d):
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            return True
    return False

=======
Suggestion 3

def main():
    n = int(input())
    dice = []
    for i in range(n):
        dice.append(list(map(int, input().split())))
    for i in range(n-2):
        if dice[i][0] == dice[i][1] and dice[i+1][0] == dice[i+1][1] and dice[i+2][0] == dice[i+2][1]:
            print('Yes')
            return
    print('No')

=======
Suggestion 4

def main():
    N = int(input())
    d = []
    for i in range(N):
        d.append(list(map(int, input().split())))
    for i in range(N-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            print('Yes')
            break
    else:
        print('No')

=======
Suggestion 5

def main():
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            print('Yes')
            return
    print('No')

=======
Suggestion 6

def main():
    N = int(input())
    d = []
    for i in range(N):
        d.append(input().split())
    flag = 0
    for i in range(N-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            flag = 1
    if flag == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def check(n, d):
    for i in range(n-2):
        if d[i][0]==d[i][1] and d[i+1][0]==d[i+1][1] and d[i+2][0]==d[i+2][1]:
            return True
    return False

n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]
print("Yes" if check(n, d) else "No")

=======
Suggestion 8

def main():
    n = int(input())
    d = []
    for i in range(n):
        d.append(list(map(int, input().split())))
    flag = False
    for i in range(n - 2):
        if d[i][0] == d[i][1] and d[i + 1][0] == d[i + 1][1] and d[i + 2][0] == d[i + 2][1]:
            flag = True
            break
    if flag:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    N = int(input())
    D = []
    for i in range(N):
        D.append(list(map(int, input().split())))

    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
            print("Yes")
            return
    print("No")

=======
Suggestion 10

def main():
    n = int(input())
    d = []
    for i in range(n):
        d.append(list(map(int,input().split())))
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            print('Yes')
            exit()
    print('No')
