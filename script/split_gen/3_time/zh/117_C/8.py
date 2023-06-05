def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n == 1:
        print(abs(x[0] - x[-1]))
        return
    x_min = x[0]
    x_max = x[-1]
    x_min_index = 0
    x_max_index = n - 1
    x_min_move = 0
    x_max_move = 0
    for i in range(n):
        if x[i] < 0:
            x_min_move += abs(x[i])
            x_min_index = i
        else:
            x_max_move += abs(x[i])
            x_max_index = i
    if x_min_index == 0 and x_max_index == n - 1:
        print(x_max_move - x_min_move)
    elif x_min_index == 0:
        print(x_max_move - x_min_move + abs(x[x_max_index]))
    elif x_max_index == n - 1:
        print(x_max_move - x_min_move + abs(x[x_min_index]))
    else:
        print(x_max_move - x_min_move + abs(x[x_max_index]) + abs(x[x_min_index]))
