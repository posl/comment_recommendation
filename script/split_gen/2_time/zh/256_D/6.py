def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.sort(key=lambda x: x[0])
    result = []
    result.append(l[0])
    for i in range(1, n):
        if result[-1][1] < l[i][0]:
            result.append(l[i])
        else:
            result[-1][1] = max(result[-1][1], l[i][1])
    for i in range(len(result)):
        print(result[i][0], result[i][1])
