def get_input():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    return N, S

if __name__ == '__main__':
    get_input()