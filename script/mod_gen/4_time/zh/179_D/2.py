def get_input():
    n, k = map(int, input().split())
    lrs = []
    for i in range(k):
        lrs.append(list(map(int, input().split())))
    return n, k, lrs

if __name__ == '__main__':
    get_input()