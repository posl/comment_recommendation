def get_input():
    X = input()
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    return X, N, S

if __name__ == '__main__':
    get_input()