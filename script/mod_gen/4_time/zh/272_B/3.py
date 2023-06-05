def get_input():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(m)]
    return n, m, a

if __name__ == '__main__':
    get_input()