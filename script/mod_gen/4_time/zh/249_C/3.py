def get_input():
    N, K = map(int, input().split())
    S = []
    for i in range(N):
        S.append(input())
    return N, K, S

if __name__ == '__main__':
    get_input()