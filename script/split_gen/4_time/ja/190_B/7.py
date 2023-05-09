def main():
    n, s, d = map(int, input().split())
    x = []
    y = []
    for i in range(n):
        tmp_x, tmp_y = map(int, input().split())
        x.append(tmp_x)
        y.append(tmp_y)
    for i in range(n):
        if x[i] < s and y[i] > d:
            print("Yes")
            return
    print("No")
    return
