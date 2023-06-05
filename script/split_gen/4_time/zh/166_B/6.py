def main():
    n, k = map(int, input().split())
    a = []
    for i in range(k):
        a.append(list(map(int, input().split())))
    snuke = [0] * n
    for i in range(k):
        for j in range(a[i][0]):
            snuke[a[i][j + 1] - 1] += 1
    print(snuke.count(0))
