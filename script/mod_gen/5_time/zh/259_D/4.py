def get_input():
    N = int(input())
    S_X, S_Y, T_X, T_Y = map(int, input().split())
    circles = []
    for i in range(N):
        circles.append(list(map(int, input().split())))
    return N, S_X, S_Y, T_X, T_Y, circles

if __name__ == '__main__':
    get_input()