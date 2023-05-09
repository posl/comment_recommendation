def get_input():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    return h, w, a

if __name__ == '__main__':
    get_input()