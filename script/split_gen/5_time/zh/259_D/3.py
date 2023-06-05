def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    xyr = []
    for i in range(N):
        xyr.append(list(map(int, input().split())))
    print(xyr)
