def second_highest_mountain():
    N = int(input())
    mountains = []
    for i in range(N):
        mountains.append(input().split())
    mountains.sort(key=lambda x:int(x[1]),reverse=True)
    print(mountains[1][0])

if __name__ == '__main__':
    second_highest_mountain()