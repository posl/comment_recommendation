def main():
    n = int(input())
    data = [input().split() for i in range(n)]
    data = [[s, int(t), i] for i, (s, t) in enumerate(data)]
    data.sort(key=lambda x: x[1], reverse=True)
    data.sort(key=lambda x: x[0])
    for i in range(1, n):
        if data[i - 1][0] == data[i][0]:
            data[i][1] = 0
    data.sort(key=lambda x: x[1], reverse=True)
    print(data[0][2] + 1)
