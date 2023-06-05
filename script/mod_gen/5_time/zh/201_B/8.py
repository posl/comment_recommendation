def get_second_high_mountain():
    n = int(input())
    mountains = []
    for i in range(n):
        name, height = input().split(' ')
        mountains.append((name, int(height)))
    mountains.sort(key=lambda x: x[1], reverse=True)
    return mountains[1][0]

if __name__ == '__main__':
    get_second_high_mountain()