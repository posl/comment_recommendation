def get_input():
    n = int(input())
    x, y = map(int, input().split())
    lunch = []
    for i in range(n):
        lunch.append(tuple(map(int, input().split())))
    return n, x, y, lunch

if __name__ == '__main__':
    get_input()