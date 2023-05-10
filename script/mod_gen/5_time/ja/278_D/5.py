def get_input_data():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = []
    for q in range(Q):
        query.append(list(map(int, input().split())))
    return (N, A, Q, query)

if __name__ == '__main__':
    get_input_data()