Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 2

def main():
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            cnt += 1
    if cnt > 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    n = int(input())
    dice = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n-2):
        if dice[i][0] == dice[i][1] and dice[i+1][0] == dice[i+1][1] and dice[i+2][0] == dice[i+2][1]:
            print('Yes')
            break
    else:
        print('No')

=======
Suggestion 4

def main():
    n = int(input())
    d = []
    for i in range(n):
        d.append(list(map(int, input().split())))
    count = 0
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            count += 1
    if count > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    N = int(input())
    D = []
    for i in range(N):
        D.append(list(map(int, input().split())))
    count = 0
    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
            count += 1
    if count > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n = int(input())
    dice = []
    for i in range(n):
        dice.append(list(map(int, input().split())))

    count = 0
    for i in range(n-2):
        if dice[i][0] == dice[i][1] and dice[i+1][0] == dice[i+1][1] and dice[i+2][0] == dice[i+2][1]:
            count += 1
    if count >= 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    N = int(input())
    ans = 'No'
    cnt = 0
    for i in range(N):
        D1, D2 = map(int, input().split())
        if D1 == D2:
            cnt += 1
        else:
            cnt = 0
        if cnt >= 3:
            ans = 'Yes'
            break
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    dice = []
    for i in range(N):
        dice.append(list(map(int, input().split())))
    cnt = 0
    for i in range(N-2):
        if dice[i][0] == dice[i][1] and dice[i+1][0] == dice[i+1][1] and dice[i+2][0] == dice[i+2][1]:
            cnt += 1
    if cnt > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def problem179b():
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            cnt += 1
    if cnt > 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    n = int(input())
    dice = []
    flag = False

    for i in range(n):
        dice.append(list(map(int, input().split())))

    for i in range(n-2):
        if dice[i][0] == dice[i][1] and dice[i+1][0] == dice[i+1][1] and dice[i+2][0] == dice[i+2][1]:
            flag = True
            break

    if flag:
        print("Yes")
    else:
        print("No")
