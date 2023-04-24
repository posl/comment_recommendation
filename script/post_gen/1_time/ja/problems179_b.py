Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    cnt = 0
    for i in range(n):
        d1, d2 = map(int, input().split())
        if d1 == d2:
            cnt += 1
        else:
            cnt = 0
        if cnt >= 3:
            print("Yes")
            return
    print("No")

=======
Suggestion 2

def main():
    N = int(input())
    count = 0
    for i in range(N):
        D1, D2 = map(int, input().split())
        if D1 == D2:
            count += 1
        else:
            count = 0
        if count >= 3:
            print('Yes')
            return
    print('No')
    return

=======
Suggestion 3

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

main()

=======
Suggestion 4

def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    ans = "No"
    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
            ans = "Yes"
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N-2):
        if D[i][0] == D[i][1] == D[i+1][0] == D[i+1][1] == D[i+2][0] == D[i+2][1]:
            cnt += 1
    if cnt > 0:
        print('Yes')
    else:
        print('No')

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

=======
Suggestion 7

def main():
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n-2):
        if d[i][0] == d[i][1] == d[i+1][0] == d[i+1][1] == d[i+2][0] == d[i+2][1]:
            print('Yes')
            return
    print('No')

=======
Suggestion 8

def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]

    ans = "No"
    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
            ans = "Yes"
            break

    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    zoro = 0
    for _ in range(N):
        d1, d2 = map(int, input().split())
        if d1 == d2:
            zoro += 1
            if zoro == 3:
                print("Yes")
                return
        else:
            zoro = 0
    print("No")

=======
Suggestion 10

def main():
    n = int(input())
    d = [list(map(int, input().split())) for i in range(n)]
    ans = "No"
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            ans = "Yes"
            break
    print(ans)
