def read_data():
    h, w, c = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    return h, w, c, a

if __name__ == '__main__':
    read_data()