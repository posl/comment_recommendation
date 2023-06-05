def get_input():
    n, m = map(int, input().split())
    b = []
    for _ in range(n):
        b.append(list(map(int, input().split())))
    return n, m, b

if __name__ == '__main__':
    get_input()