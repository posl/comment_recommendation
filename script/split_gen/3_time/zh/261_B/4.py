def main():
    n = int(input())
    a = [input() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] == "W":
                if a[j][i] != "L":
                    print("不正确")
                    return
            elif a[i][j] == "L":
                if a[j][i] != "W":
                    print("不正确")
                    return
            elif a[i][j] == "D":
                if a[j][i] != "D":
                    print("不正确")
                    return
    print("正确")
