def main():
    N = int(input())
    XY = []
    for i in range(N):
        x, y = map(int, input().split())
        XY.append((x, y))
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if is_on_same_line(XY[i], XY[j], XY[k]):
                    print("Yes")
                    return
    print("No")
