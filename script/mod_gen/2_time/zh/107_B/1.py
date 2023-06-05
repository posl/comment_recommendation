def get_input():
    h, w = input().split()
    h = int(h)
    w = int(w)
    a = []
    for i in range(h):
        a.append(input())
    return h, w, a

if __name__ == '__main__':
    get_input()