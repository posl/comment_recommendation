def get_input():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    return Q, query

if __name__ == '__main__':
    get_input()