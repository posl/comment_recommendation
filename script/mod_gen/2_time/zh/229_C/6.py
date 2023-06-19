def get_input():
    n, w = map(int, input().split())
    cheese = []
    for _ in range(n):
        cheese.append(list(map(int, input().split())))
    return n, w, cheese

if __name__ == '__main__':
    get_input()