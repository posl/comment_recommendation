def get_input():
    h, w = input().split(" ")
    h = int(h)
    w = int(w)
    h1, w1 = input().split(" ")
    h1 = int(h1)
    w1 = int(w1)
    return h, w, h1, w1

if __name__ == '__main__':
    get_input()