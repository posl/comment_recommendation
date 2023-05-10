def get_input():
    n,m = map(int, input().split())
    roads = []
    for _ in range(m):
        roads.append([int(x) for x in input().split()])
    return n, roads

if __name__ == '__main__':
    get_input()