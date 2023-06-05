def get_input():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    return N, A, Q, query

if __name__ == '__main__':
    get_input()