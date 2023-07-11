def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(input())
    for i in range(n):
        for j in range(n):
            if i != j:
                if a[i][j] == 'W' and a[j][i] != 'L':
                    print('incorrect')
