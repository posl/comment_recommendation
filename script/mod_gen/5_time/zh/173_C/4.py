def get_input():
    h, w, k = map(int, input().split())
    c = []
    for i in range(h):
        c.append(list(input()))
    return h, w, k, c

if __name__ == '__main__':
    get_input()