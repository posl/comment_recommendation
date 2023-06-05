def get_input():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    Query = []
    for i in range(Q):
        Query.append(list(map(int, input().split())))
    return N, A, Q, Query

if __name__ == '__main__':
    get_input()