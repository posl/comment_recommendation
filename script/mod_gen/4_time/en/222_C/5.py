def get_input():
    n, m = map(int, input().split())
    a = [input() for _ in range(2 * n)]
    return n, m, a

if __name__ == '__main__':
    get_input()