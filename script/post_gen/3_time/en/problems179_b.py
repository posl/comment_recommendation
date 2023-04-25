Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    doublets = 0
    for _ in range(n):
        d1, d2 = map(int, input().split())
        if d1 == d2:
            doublets += 1
        else:
            doublets = 0
        if doublets >= 3:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 2

def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N-2):
        if D[i][0] == D[i][1] == D[i+1][0] == D[i+1][1] == D[i+2][0] == D[i+2][1]:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 3

def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N - 2):
        if D[i][0] == D[i][1] and D[i + 1][0] == D[i + 1][1] and D[i + 2][0] == D[i + 2][1]:
            print('Yes')
            return
    print('No')

main()

=======
Suggestion 4

def main():
    N = int(input())
    D = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 5

def main():
    N = int(input())
    D = [list(map(int, input().split())) for i in range(N)]
    for i in range(N - 2):
        if D[i][0] == D[i][1] == D[i + 1][0] == D[i + 1][1] == D[i + 2][0] == D[i + 2][1]:
            print('Yes')
            return
    print('No')
    return

=======
Suggestion 6

def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    ans = 'No'
    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
            ans = 'Yes'
            break
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    D = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N-2):
        if D[i][0]==D[i][1] and D[i+1][0]==D[i+1][1] and D[i+2][0]==D[i+2][1]:
            print("Yes")
            break
    else:
        print("No")

=======
Suggestion 8

def main():
    N = int(input())
    D = [list(map(int,input().split())) for i in range(N)]
    for i in range(N-2):
        if D[i][0]==D[i][1] and D[i+1][0]==D[i+1][1] and D[i+2][0]==D[i+2][1]:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 9

def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    #print(D)
    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 10

def main():
    #入力
    n = int(input())
    d = [list(map(int, input().split())) for i in range(n)]

    #処理
    count = 0
    for i in range(n):
        if d[i][0] == d[i][1]:
            count += 1
            if count == 3:
                print("Yes")
                return
        else:
            count = 0
    print("No")
    return
