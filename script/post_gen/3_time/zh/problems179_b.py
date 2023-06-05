Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    dice = []
    for i in range(N):
        dice.append([int(x) for x in input().split()])
    #print(dice)
    for i in range(N-2):
        if dice[i][0] == dice[i][1] and dice[i+1][0] == dice[i+1][1] and dice[i+2][0] == dice[i+2][1]:
            print("Yes")
            return
    print("No")

=======
Suggestion 2

def main():
    n = int(input())
    d = []
    for i in range(n):
        d.append(list(map(int, input().split())))
    for i in range(n - 2):
        if d[i][0] == d[i][1] and d[i + 1][0] == d[i + 1][1] and d[i + 2][0] == d[i + 2][1]:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 3

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
Suggestion 4

def main():
    n = int(input())
    d = []
    for i in range(n):
        d.append(list(map(int, input().split())))
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            print('Yes')
            return
    print('No')
    return

=======
Suggestion 5

def main():
    n = int(input())
    ans = "No"
    count = 0
    for i in range(n):
        d1, d2 = map(int,input().split())
        if d1 == d2:
            count += 1
            if count == 3:
                ans = "Yes"
                break
        else:
            count = 0
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    d = []
    for i in range(n):
        d.append(list(map(int, input().split())))
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            print('Yes')
            return
    print('No')

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
            break
    else:
        print("No")

=======
Suggestion 8

def main():
    n = int(input())
    d = []
    for i in range(n):
        d.append(list(map(int, input().split())))
    for i in range(n - 2):
        if d[i][0] == d[i][1] and d[i + 1][0] == d[i + 1][1] and d[i + 2][0] == d[i + 2][1]:
            print("Yes")
            return
    print("No")

=======
Suggestion 9

def main():
    n = int(input())
    dice = []
    for i in range(n):
        dice.append([int(x) for x in input().split()])
    for i in range(n-2):
        if dice[i][0] == dice[i][1] and dice[i+1][0] == dice[i+1][1] and dice[i+2][0] == dice[i+2][1]:
            print("Yes")
            return
    print("No")

=======
Suggestion 10

def main():
    n = int(input())
    d = [list(map(int, input().split())) for i in range(n)]
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            print("Yes")
            exit()
    print("No")

main()
