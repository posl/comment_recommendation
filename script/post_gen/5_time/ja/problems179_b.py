Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    D = []
    for i in range(N):
        D.append(list(map(int, input().split())))

    count = 0
    for i in range(N - 2):
        if D[i][0] == D[i][1] and D[i + 1][0] == D[i + 1][1] and D[i + 2][0] == D[i + 2][1]:
            count += 1

    if count >= 1:
        print('Yes')
    else:
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
            return
    print("No")
    return

=======
Suggestion 3

def main():
    n = int(input())
    d = []
    for i in range(n):
        d.append(list(map(int, input().split())))

    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 4

def main():
    n = int(input())
    dice = [list(map(int,input().split())) for _ in range(n)]
    count = 0
    for i in range(n-2):
        if dice[i][0] == dice[i][1] and dice[i+1][0] == dice[i+1][1] and dice[i+2][0] == dice[i+2][1]:
            count += 1
        else:
            pass
    if count >= 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            cnt += 1
    if cnt >= 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    n = int(input())
    cnt = 0
    for i in range(n):
        a, b = map(int, input().split())
        if a == b:
            cnt += 1
            if cnt == 3:
                print('Yes')
                return
        else:
            cnt = 0
    print('No')

=======
Suggestion 7

def main():
    n = int(input())
    dice = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n - 2):
        if dice[i][0] == dice[i][1] and dice[i + 1][0] == dice[i + 1][1] and dice[i + 2][0] == dice[i + 2][1]:
            print('Yes')
            return
    print('No')

=======
Suggestion 8

def main():
    n = int(input())
    ans = 'No'
    count = 0
    for i in range(n):
        d1, d2 = map(int, input().split())
        if d1 == d2:
            count += 1
        else:
            count = 0
        if count >= 3:
            ans = 'Yes'
    print(ans)

=======
Suggestion 9

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
