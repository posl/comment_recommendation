Synthesizing 9/10 solutions

=======
Suggestion 1

def getSecondHeight(heights):
    heights.sort()
    return heights[-2]

=======
Suggestion 2

def main():
    n = int(input())
    mountains = []
    for i in range(n):
        mountains.append(input().split())
    mountains.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountains[1][0])

=======
Suggestion 3

def getSecondHeight(heights):
    heights.sort(reverse=True)
    return heights[1]

=======
Suggestion 4

def find_second_highest_mountain(mountain_list):
    highest = 0
    second_highest = 0
    highest_mountain = ''
    second_highest_mountain = ''
    for mountain in mountain_list:
        if mountain[1] > highest:
            second_highest = highest
            second_highest_mountain = highest_mountain
            highest = mountain[1]
            highest_mountain = mountain[0]
        elif mountain[1] > second_highest:
            second_highest = mountain[1]
            second_highest_mountain = mountain[0]
    return second_highest_mountain

=======
Suggestion 5

def main():
    N = int(input())
    mountains = []
    for i in range(N):
        S, T = input().split()
        T = int(T)
        mountains.append((S, T))
    mountains.sort(key=lambda x: -x[1])
    print(mountains[1][0])

=======
Suggestion 6

def main():
    # 读取输入
    n = int(input())
    mountains = []
    for i in range(n):
        mountains.append(input().split())
    # 计算输出
    mountains.sort(key = lambda x: int(x[1]), reverse = True)
    print(mountains[1][0])

=======
Suggestion 7

def main():
    n = int(input())
    mountains = []
    for i in range(n):
        s, t = input().split()
        mountains.append((s, int(t)))
    mountains.sort(key=lambda x: x[1])
    print(mountains[-2][0])

=======
Suggestion 8

def main():
    n = int(input())
    mountains = []
    for i in range(n):
        s, t = input().split()
        mountains.append((s, int(t)))
    mountains.sort(key=lambda x: x[1], reverse=True)
    print(mountains[1][0])

=======
Suggestion 9

def get_second_high_mountain():
    n = int(input())
    mountains = []
    for i in range(n):
        name, height = input().split(' ')
        mountains.append((name, int(height)))
    mountains.sort(key=lambda x: x[1], reverse=True)
    return mountains[1][0]
