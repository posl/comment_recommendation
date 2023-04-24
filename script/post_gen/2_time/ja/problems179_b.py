Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n)]
    count = 0
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            count += 1
    if count >= 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    n = int(input())
    dice = []
    for i in range(n):
        dice.append(list(map(int, input().split())))
    count = 0
    for i in range(n-2):
        if dice[i][0] == dice[i][1] and dice[i+1][0] == dice[i+1][1] and dice[i+2][0] == dice[i+2][1]:
            count += 1
            break
    if count == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    n = int(input())
    dice = []
    for i in range(n):
        dice.append(list(map(int, input().split())))

    for i in range(n-2):
        if (dice[i][0] == dice[i][1]) and (dice[i+1][0] == dice[i+1][1]) and (dice[i+2][0] == dice[i+2][1]):
            print("Yes")
            exit()
    print("No")

=======
Suggestion 4

def main():
    N = int(input())
    D = [list(map(int,input().split())) for _ in range(N)]
    ans = 'No'
    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
            ans = 'Yes'
            break
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    dice = [input().split() for _ in range(N)]
    cnt = 0
    for i in range(N-2):
        if dice[i][0] == dice[i][1] and dice[i+1][0] == dice[i+1][1] and dice[i+2][0] == dice[i+2][1]:
            cnt += 1
    if cnt > 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    N = int(input())
    D = [list(map(int, input().split())) for i in range(N)]

    ans = 'No'
    cnt = 0
    for i in range(N):
        if D[i][0] == D[i][1]:
            cnt += 1
        else:
            cnt = 0
        if cnt >= 3:
            ans = 'Yes'
            break

    print(ans)

=======
Suggestion 7

def check():
    n = int(input())
    d = []
    for i in range(n):
        d.append(list(map(int, input().split())))
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            return "Yes"
    return "No"

print(check())

=======
Suggestion 8

def main():
    num = int(input())
    dice = []
    for i in range(num):
        dice.append(list(map(int, input().split())))
    cnt = 0
    for i in range(num-2):
        if dice[i][0] == dice[i][1] and dice[i+1][0] == dice[i+1][1] and dice[i+2][0] == dice[i+2][1]:
            cnt += 1
            break
    if cnt > 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def check():
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
Suggestion 10

def check_zorome(arr):
    count = 1
    for i in range(len(arr)-1):
        if arr[i][0] == arr[i+1][0]:
            count += 1
            if count == 3:
                return True
        else:
            count = 1
    return False
