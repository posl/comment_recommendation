def check(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == "W":
                if a[j][i] != "L":
                    return False
            elif a[i][j] == "L":
