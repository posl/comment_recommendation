def read_input():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    return n, m, s

if __name__ == '__main__':
    read_input()