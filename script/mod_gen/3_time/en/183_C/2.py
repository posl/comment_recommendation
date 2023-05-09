def get_input():
    n, k = map(int, input().split())
    t = []
    for i in range(n):
        t.append(list(map(int, input().split())))
    return n, k, t

if __name__ == '__main__':
    get_input()