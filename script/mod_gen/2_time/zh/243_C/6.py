def get_input():
    N = int(input())
    XY = []
    for _ in range(N):
        XY.append(list(map(int, input().split())))
    S = input()
    return N, XY, S

if __name__ == '__main__':
    get_input()