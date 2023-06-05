def get_input():
    h, w = map(int, input().split())
    g = []
    for i in range(h):
        g.append(input())
    return h, w, g

if __name__ == '__main__':
    get_input()