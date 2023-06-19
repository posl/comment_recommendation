def get_input():
    N, K = map(int, input().split())
    P = []
    for i in range(N):
        P.append(list(map(int, input().split())))
    return N, K, P

if __name__ == '__main__':
    get_input()