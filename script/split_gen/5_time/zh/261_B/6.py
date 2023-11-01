def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(input()))
    for i in range(n):
        for j in range(n):
            if a[i][j] == "W":
                if a[j][i] != "L":
                    print("incorrect")
                    return
            elif a[i][j] == "L":
                if a[j][i] != "W":
                    print("incorrect")
                    return
            elif a
