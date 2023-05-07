def main():
    n = int(input())
    xy = []
    for i in range(n):
        x, y = map(int, input().split())
        xy.append([x, y])
    s = input()
    for i in range(n):
        if s[i] == "L":
            for j in range(i+1, n):
                if s[j] == "L":
                    if xy[i][0] > xy[j][0]:
                        print("Yes")
                        return
                    elif xy[i][0] == xy[j][0] and xy[i][1] > xy[j][1]:
                        print("Yes")
                        return
                elif s[j] == "R":
                    if xy[i][0] > xy[j][0] and xy[i][1] == xy[j][1]:
                        print("Yes")
                        return
        elif s[i] == "R":
            for j in range(i+1, n):
                if s[j] == "R":
                    if xy[i][0] < xy[j][0]:
                        print("Yes")
                        return
                    elif xy[i][0] == xy[j][0] and xy[i][1] > xy[j][1]:
                        print("Yes")
                        return
                elif s[j] == "L":
                    if xy[i][0] < xy[j][0] and xy[i][1] == xy[j][1]:
                        print("Yes")
                        return
    print("No")
