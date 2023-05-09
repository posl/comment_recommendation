Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
            print('Yes')
            return
    print('No')

=======
Suggestion 2

def main():
    n = int(input())
    d = []
    for i in range(n):
        d.append(list(map(int, input().split())))
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 3

def main():
    N = int(input())
    D = []
    for i in range(N):
        D.append(list(map(int, input().split())))
    count = 0
    for i in range(N):
        if D[i][0] == D[i][1]:
            count += 1
            if count == 3:
                print("Yes")
                return
        else:
            count = 0
    print("No")

=======
Suggestion 4

def main():
    N = int(input())
    D = []
    for i in range(N):
        D.append(input().split())
    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
            print("Yes")
            return
    print("No")

=======
Suggestion 5

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
Suggestion 6

def main():
    N=int(input())
    flag=False
    count=0
    for i in range(N):
        a,b=map(int,input().split())
        if a==b:
            count+=1
            if count>=3:
                flag=True
        else:
            count=0
    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    n = int(input())
    dice_list = []
    for i in range(n):
        dice_list.append(list(map(int, input().split())))
    count = 0
    for i in range(n):
        if dice_list[i][0] == dice_list[i][1]:
            count += 1
            if count == 3:
                print('Yes')
                exit()
        else:
            count = 0
    print('No')

=======
Suggestion 8

def main():
    # input
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n)]

    # compute

    # output
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 9

def check_doublets():
    N = int(input())
    D = [list(map(int, input().split())) for i in range(N)]
    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
            print('Yes')
            break
    else:
        print('No')
        
check_doublets()

=======
Suggestion 10

def main():
    n = int(input())
    dice = []
    for i in range(n):
        a,b = input().split()
        dice.append([int(a),int(b)])
    count = 0
    for j in range(n-2):
        if dice[j][0] == dice[j][1] and dice[j+1][0] == dice[j+1][1] and dice[j+2][0] == dice[j+2][1]:
            count += 1
    if count > 0:
        print("Yes")
    else:
        print("No")
