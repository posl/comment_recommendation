def main():
    a = []
    for i in range(10):
        a.append(input())
    for i in range(10):
        for j in range(10):
            if a[i][j] == '#':
                print(i+1,j+1)
                return
