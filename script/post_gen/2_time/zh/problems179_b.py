Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    d = [list(map(int, input().split())) for i in range(n)]
    flag = False
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            flag = True
            break
    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    n = int(input())
    count = 0
    for i in range(n):
        d1, d2 = map(int, input().split())
        if d1 == d2:
            count += 1
            if count >= 3:
                print("Yes")
                return
        else:
            count = 0
    print("No")

=======
Suggestion 3

def main():
    n = int(input())
    count = 0
    for i in range(0, n):
        a, b = map(int, input().split())
        if a == b:
            count += 1
        else:
            count = 0
        if count >= 3:
            break
    if count >= 3:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    num = int(input())
    last = 0
    count = 0
    for i in range(num):
        a, b = map(int, input().split())
        if a == b:
            count += 1
            if count == 3:
                print("Yes")
                return
        else:
            count = 0
        last = a
    print("No")

=======
Suggestion 5

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
Suggestion 6

def main():
    n = int(input())
    dice = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n - 2):
        if dice[i][0] == dice[i][1] and dice[i + 1][0] == dice[i + 1][1] and dice[i + 2][0] == dice[i + 2][1]:
            cnt += 1
    print("Yes" if cnt > 0 else "No")

=======
Suggestion 7

def main():
    n = int(input())
    flag = False
    count = 0
    for i in range(n):
        d1, d2 = map(int, input().split())
        if d1 == d2:
            count += 1
        else:
            count = 0
        if count >= 3:
            flag = True
    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

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

=======
Suggestion 9

def main():
    n = int(input())
    dice = []
    for i in range(n):
        dice.append(list(map(int, input().split())))
    for i in range(n-2):
        if dice[i][0] == dice[i][1] and dice[i+1][0] == dice[i+1][1] and dice[i+2][0] == dice[i+2][1]:
            print("Yes")
            return
    print("No")

=======
Suggestion 10

def main():
    N = int(input())
    D = []
    for i in range(N):
        D.append(list(map(int, input().split())))
    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
            print("Yes")
            break
    else:
        print("No")
