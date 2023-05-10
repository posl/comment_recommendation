def check_correctness(n, a):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a[i][j] == "W":
                if a[j][i] != "L":
                    return False
            elif a[i][j] == "L":
                if a[j][i] != "W":
                    return False
            else:
                if a[j][i] != "D":
                    return False
    return True
n = int(input())
a = [input() for _ in range(n)]

if __name__ == '__main__':
    check_correctness()