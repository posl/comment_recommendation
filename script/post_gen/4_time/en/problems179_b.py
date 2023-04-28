Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
            print("Yes")
            return
    print("No")

=======
Suggestion 2

def main():
    n = int(input())
    dice = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n-2):
        if dice[i][0] == dice[i][1] and dice[i+1][0] == dice[i+1][1] and dice[i+2][0] == dice[i+2][1]:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 3

def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 4

def main():
    N = int(input())
    dice = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        if dice[i][0] == dice[i][1]:
            cnt += 1
        else:
            cnt = 0
        if cnt == 3:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 5

def main():
    N = int(input())
    D = []
    for i in range(N):
        D.append(list(map(int,input().split())))
    cnt = 0
    for i in range(N):
        if D[i][0] == D[i][1]:
            cnt += 1
            if cnt >= 3:
                print('Yes')
                exit()
        else:
            cnt = 0
    print('No')

=======
Suggestion 6

def solve():
    N = int(input())
    D = []
    for i in range(N):
        D.append(list(map(int, input().split())))

    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 7

def main():
    N = int(input())
    dice = []
    for i in range(N):
        dice.append(list(map(int, input().split())))
    for i in range(N - 2):
        if dice[i][0] == dice[i][1] and dice[i + 1][0] == dice[i + 1][1] and dice[i + 2][0] == dice[i + 2][1]:
            print("Yes")
            exit(0)
    print("No")

=======
Suggestion 8

def main():
    N = int(input())
    doublets = 0
    for i in range(N):
        dice = input().split()
        if dice[0] == dice[1]:
            doublets += 1
        else:
            doublets = 0
        if doublets == 3:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 9

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
Suggestion 10

def main():
    # Get input here
    N = int(input())
    doublets = []
    for _ in range(N):
        doublets.append(input().split())

    # Calculate result here
    count = 0
    for i in range(N):
        if doublets[i][0] == doublets[i][1]:
            count += 1
            if count == 3:
                break
        else:
            count = 0

    # Print result here
    if count == 3:
        print('Yes')
    else:
        print('No')
