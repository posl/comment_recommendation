def get_input():
    h, w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    return h, w, s

if __name__ == '__main__':
    get_input()