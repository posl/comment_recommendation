Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
            count += 1
    if count >= 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    N = int(input())
    D = [list(map(int,input().split())) for i in range(N)]
    cnt = 0
    for i in range(N):
        if D[i][0] == D[i][1]:
            cnt += 1
        else:
            cnt = 0
        if cnt == 3:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 3

def main():
    N = int(input())
    D = [list(map(int,input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N-2):
        if D[i][0] == D[i][1] == D[i+1][0] == D[i+1][1] == D[i+2][0] == D[i+2][1]:
            cnt += 1
    if cnt > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]

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
Suggestion 5

def main():
    n = int(input())
    d = [list(map(int,input().split())) for i in range(n)]

    ans = "No"
    for i in range(n-2):
        if d[i][0] == d[i][1] == d[i+1][0] == d[i+1][1] == d[i+2][0] == d[i+2][1]:
            ans = "Yes"
            break

    print(ans)

=======
Suggestion 6

def   main (): 
     n   =   int ( input ()) 
     d   =   [ list ( map ( int ,   input (). split ()))   for   _   in   range ( n )] 
     ans   =   'No' 
     for   i   in   range ( n - 2 ): 
         if   d [ i ][ 0 ]   ==   d [ i ][ 1 ]   ==   d [ i + 1 ][ 0 ]   ==   d [ i + 1 ][ 1 ]   ==   d [ i + 2 ][ 0 ]   ==   d [ i + 2 ][ 1 ]: 
             ans   =   'Yes' 
     print ( ans )

=======
Suggestion 7

def main():
    N = int(input())
    D = []
    for i in range(N):
        D.append(list(map(int,input().split())))
    print(D)
    for i in range(N-2):
        if D[i][0] == D[i][1] == D[i+1][0] == D[i+1][1] == D[i+2][0] == D[i+2][1]:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 8

def main():
  N = int(input())
  D = []
  for i in range(N):
    D.append(list(map(int, input().split())))
  count = 0
  for i in range(N):
    if D[i][0] == D[i][1]:
      count += 1
    else:
      count = 0
    if count >= 3:
      print("Yes")
      return
  print("No")

=======
Suggestion 9

def main():
    #入力
    n = int(input())
    d = []
    for i in range(n):
        d.append(list(map(int,input().split())))
    #処理
    ans = "No"
    for i in range(n-2):
        if d[i][0]==d[i][1]==d[i+1][0]==d[i+1][1]==d[i+2][0]==d[i+2][1]:
            ans = "Yes"
            break
    #出力
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    D = [list(map(int,input().split())) for _ in range(N)]
    #print(D)
    if N <= 2:
        print("No")
        return
    for i in range(N-2):
        if D[i][0] == D[i][1] == D[i+1][0] == D[i+1][1] == D[i+2][0] == D[i+2][1]:
            print("Yes")
            return
    print("No")
