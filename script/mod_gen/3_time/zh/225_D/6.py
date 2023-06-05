def get_input():
    n, q = map(int, input().split())
    query = []
    for i in range(q):
        query.append(list(map(int, input().split())))
    return n, q, query

if __name__ == '__main__':
    get_input()