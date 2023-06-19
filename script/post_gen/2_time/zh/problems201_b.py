Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    mountains = []
    for i in range(n):
        mountains.append(input().split())
    mountains.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountains[1][0])

=======
Suggestion 2

def getSecondMaxMountainName():
    mountains = []
    N = int(input())
    for i in range(N):
        mountains.append(input().split())
    mountains.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountains[1][0])


getSecondMaxMountainName()

=======
Suggestion 3

def read_input():
    n = int(input())
    mountains = []
    for i in range(n):
        s, t = input().split()
        mountains.append((s, int(t)))
    return mountains

=======
Suggestion 4

def get_second_height_mountain_number(n, height_list):
    height_list.sort(reverse=True)
    return height_list[1][0]

=======
Suggestion 5

def second_highest_mountain():
    N = int(input())
    mountains = []
    for _ in range(N):
        name, height = input().split()
        height = int(height)
        mountains.append((name, height))
    mountains = sorted(mountains, key=lambda x: x[1], reverse=True)
    print(mountains[1][0])

=======
Suggestion 6

def main():
    N = int(input())
    mountains = []
    for i in range(N):
        mountains.append(input().split())
    mountains.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountains[1][0])

=======
Suggestion 7

def main():
    N = int(input())
    mountain = []
    for i in range(N):
        mountain.append(input().split())
    mountain.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountain[1][0])

=======
Suggestion 8

def main():
    N = int(input())
    mountains = []
    for i in range(N):
        mountain = input().split()
        mountain[1] = int(mountain[1])
        mountains.append(mountain)
    mountains.sort(key=lambda x: x[1], reverse=True)
    print(mountains[1][0])

=======
Suggestion 9

def main():
    # 读入数据
    N = int(input())
    ST = []
    for i in range(N):
        ST.append(input().split())
    # 由于ST中的第二个元素是字符串，所以需要转换成数字才能进行排序
    for i in range(N):
        ST[i][1] = int(ST[i][1])
    # 按照山的高度排序
    ST.sort(key=lambda x: x[1], reverse=True)
    # 打印第二高的山的名字
    print(ST[1][0])

=======
Suggestion 10

def main():
    n = int(input())
    mountains = []
    for i in range(n):
        name, height = input().split()
        mountains.append([name, int(height)])
    mountains.sort(key=lambda x: x[1], reverse=True)
    print(mountains[1][0])
