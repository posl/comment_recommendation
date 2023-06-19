def second_highest_mountain():
    N = int(input())
    mountains = []
    for _ in range(N):
        name, height = input().split()
        height = int(height)
        mountains.append((name, height))
    mountains = sorted(mountains, key=lambda x: x[1], reverse=True)
    print(mountains[1][0])

if __name__ == '__main__':
    second_highest_mountain()