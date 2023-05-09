def get_input():
    h, w = map(int, input().split())
    grid = []
    for i in range(h):
        grid.append(input())
    return h, w, grid

if __name__ == '__main__':
    get_input()