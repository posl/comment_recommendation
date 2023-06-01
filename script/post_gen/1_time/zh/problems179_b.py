Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    n = int(input())
    d = []
    for i in range(n):
        d.append(list(map(int, input().split())))
    return n, d

=======
Suggestion 2

def main():
    n = int(input())
    d = []
    for i in range(n):
        d.append(list(map(int, input().split())))
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            print('Yes')
            break
    else:
        print('No')

=======
Suggestion 3

def main():
    n = int(input())
    d = []
    for i in range(n):
        d.append(list(map(int, input().split())))
    #print(d)
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 4

def main():
    n = int(input())
    d = []
    for i in range(n):
        d.append(list(map(int, input().split())))
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
Suggestion 5

def main():
    n = int(input())
    d = [list(map(int, input().split())) for i in range(n)]
    cnt = 0
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            cnt += 1
    if cnt >= 1:
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
    #print(dice)
    #print(dice[0][0])
    #print(dice[0][1])
    for i in range(n-2):
        if dice[i][0] == dice[i][1] and dice[i+1][0] == dice[i+1][1] and dice[i+2][0] == dice[i+2][1]:
            print("Yes")
            break
    else:
        print("No")

=======
Suggestion 7

def main():
    N = int(input())
    for i in range(N):
        d1, d2 = input().split()
        if i >= 2 and d1 == d2 and d0 == d1:
            print("Yes")
            return
        d0 = d1
    print("No")

=======
Suggestion 8

def main():
    n = int(input())
    dice = [list(map(int, input().split())) for i in range(n)]
    cnt = 0
    for i in range(n-2):
        if dice[i][0] == dice[i][1] and dice[i+1][0] == dice[i+1][1] and dice[i+2][0] == dice[i+2][1]:
            cnt += 1
    if cnt > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    n = int(input())
    d = []
    for i in range(n):
        d.append(list(map(int, input().split())))

    for i in range(n - 2):
        if d[i][0] == d[i][1] and d[i + 1][0] == d[i + 1][1] and d[i + 2][0] == d[i + 2][1]:
            print('Yes')
            return
    print('No')

=======
Suggestion 10

def main():
    n = int(input())
    d = []
    for i in range(n):
        d.append(list(map(int, input().split())))
    for i in range(0, n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            print("Yes")
            return
    print("No")
