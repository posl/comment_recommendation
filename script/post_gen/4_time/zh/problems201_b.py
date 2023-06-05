Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def getSecondHeight(height_list):
    if len(height_list) < 2:
        return None
    elif len(height_list) == 2:
        return height_list[0]
    else:
        height_list.sort(reverse=True)
        return height_list[1]

=======
Suggestion 2

def get_second_height_mountain_name(mountain):
    mountain_list = mountain.split('\n')
    mountain_list = mountain_list[1:]
    mountain_list = [m.split(' ') for m in mountain_list]
    mountain_list = [[m[0], int(m[1])] for m in mountain_list]
    mountain_list.sort(key=lambda x: x[1], reverse=True)
    return mountain_list[1][0]

=======
Suggestion 3

def main():
    n = int(input())
    h = []
    for i in range(n):
        h.append(input().split())
    h.sort(key=lambda x: int(x[1]), reverse=True)
    print(h[1][0])

=======
Suggestion 4

def main():
    n = int(input())
    mountains = []
    for i in range(n):
        mountains.append(input().split())
    mountains.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountains[1][0])

=======
Suggestion 5

def main():
    n = int(input())
    mountains = []
    for i in range(n):
        mountains.append(input().split())
    mountains = sorted(mountains, key=lambda x: int(x[1]), reverse=True)
    print(mountains[1][0])

=======
Suggestion 6

def get_second_highest_mountain_name(mountains):
    highest_mountain = 0
    second_highest_mountain = 0
    for mountain in mountains:
        if mountain[1] > highest_mountain:
            second_highest_mountain = highest_mountain
            highest_mountain = mountain[1]
        elif mountain[1] > second_highest_mountain:
            second_highest_mountain = mountain[1]

    for mountain in mountains:
        if mountain[1] == second_highest_mountain:
            return mountain[0]

=======
Suggestion 7

def main():
    n = int(input())
    mountains = []
    for i in range(n):
        mountain = input().split()
        mountain[1] = int(mountain[1])
        mountains.append(mountain)
    mountains.sort(key=lambda x: x[1], reverse=True)
    print(mountains[1][0])

=======
Suggestion 8

def get_second_highest_mountain(mountains):
    highest_mountain = [0, 0]
    second_highest_mountain = [0, 0]
    for mountain in mountains:
        if mountain[1] > highest_mountain[1]:
            second_highest_mountain = highest_mountain
            highest_mountain = mountain
        elif mountain[1] > second_highest_mountain[1]:
            second_highest_mountain = mountain
    return second_highest_mountain[0]

=======
Suggestion 9

def main():
    n = int(input())
    mountain = []
    for i in range(n):
        mountain.append(input().split())
    mountain.sort(key=lambda x: int(x[1]), reverse=True)
    print(mountain[1][0])
