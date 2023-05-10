def get_input():
    n, k = map(int, input().split())
    s = [input() for i in range(n)]
    return n, k, s

if __name__ == '__main__':
    get_input()