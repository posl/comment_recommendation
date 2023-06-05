def get_list():
    N, Q = input().split()
    N = int(N)
    Q = int(Q)
    list_N = []
    for i in range(N):
        list_N.append(input().split())
    list_Q = []
    for i in range(Q):
        list_Q.append(input().split())
    return list_N, list_Q

if __name__ == '__main__':
    get_list()