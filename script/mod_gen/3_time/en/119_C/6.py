def get_input():
    n, a, b, c = map(int, input().split())
    l = [int(input()) for i in range(n)]
    return n, a, b, c, l

if __name__ == '__main__':
    get_input()