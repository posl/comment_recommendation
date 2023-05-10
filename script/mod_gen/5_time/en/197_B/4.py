def get_input():
    h, w, x, y = map(int, input().split())
    s = [input() for i in range(h)]
    return h, w, x, y, s

if __name__ == '__main__':
    get_input()