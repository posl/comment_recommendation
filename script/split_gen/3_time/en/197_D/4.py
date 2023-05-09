def main():
    N = int(input())
    x_0, y_0 = map(int, input().split())
    x_N_2, y_N_2 = map(int, input().split())
    print((x_0 + x_N_2) / 2, (y_0 + y_N_2) / 2)
