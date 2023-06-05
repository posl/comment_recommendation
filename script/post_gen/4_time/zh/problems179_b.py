Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    dice = []
    for i in range(n):
        dice.append(list(map(int, input().split())))
    #print(dice)
    flag = False
    for i in range(n - 2):
        if dice[i][0] == dice[i][1] and dice[i + 1][0] == dice[i + 1][1] and dice[i + 2][0] == dice[i + 2][1]:
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
    d = []
    for i in range(n):
        d.append(input().split())
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 3

def main():
    n=int(input())
    dice=[]
    for i in range(n):
        dice.append(list(map(int,input().split())))
    for i in range(n-2):
        if dice[i][0]==dice[i][1] and dice[i+1][0]==dice[i+1][1] and dice[i+2][0]==dice[i+2][1]:
            print("Yes")
            return
    print("No")

=======
Suggestion 4

def main():
    n = int(input())
    for i in range(n-2):
        d1,d2 = map(int,input().split())
        d3,d4 = map(int,input().split())
        d5,d6 = map(int,input().split())
        if d1 == d2 and d3 == d4 and d5 == d6:
            print('Yes')
            return
    print('No')
main()

=======
Suggestion 5

def main():
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n)]
    flag = False
    for i in range(n - 2):
        if d[i][0] == d[i][1] and d[i + 1][0] == d[i + 1][1] and d[i + 2][0] == d[i + 2][1]:
            flag = True
            break
    print('Yes' if flag else 'No')

=======
Suggestion 6

def main():
    n = int(input())
    dice = []
    for i in range(n):
        dice.append(list(map(int, input().split())))

    for i in range(n-2):
        if dice[i][0] == dice[i][1] and dice[i+1][0] == dice[i+1][1] and dice[i+2][0] == dice[i+2][1]:
            print("Yes")
            exit()

    print("No")

=======
Suggestion 7

def main():
    n = int(input())
    flag = False
    for i in range(n-2):
        d1, d2 = map(int, input().split())
        if d1 == d2:
            d3, d4 = map(int, input().split())
            if d3 == d4:
                d5, d6 = map(int, input().split())
                if d5 == d6:
                    flag = True
    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def solution():
    count = int(input())
    result = []
    for i in range(count):
        result.append(input().split(' '))
    for i in range(count-2):
        if result[i][0] == result[i][1] and result[i+1][0] == result[i+1][1] and result[i+2][0] == result[i+2][1]:
            print('Yes')
            return
    print('No')

solution()

=======
Suggestion 9

def main():
    N = int(input())
    d = []
    for i in range(N):
        d.append(list(map(int, input().split())))
    # print(d)
    for i in range(N-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            print("Yes")
            exit()
    print("No")
