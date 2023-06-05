def get_input():
    n = int(input())
    x, y = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    return n, x, y, ab

if __name__ == '__main__':
    get_input()