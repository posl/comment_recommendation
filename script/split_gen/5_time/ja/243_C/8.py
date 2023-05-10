def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    s = input()
    x = []
    y = []
    for i in range(n):
        x.append(xy[i][0])
        y.append(xy[i][1])
    for i in range(n):
        if s[i] == "R":
            x[i] += 1
        elif s[i] == "L":
            x[i] -= 1
    for i in range(n):
        for j in range(i+1, n):
            if x[i] == x[j] and y[i] == y[j]:
                print("Yes")
                exit()
    print("No")
