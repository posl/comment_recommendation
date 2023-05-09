def main():
    n = int(input())
    lines = []
    for _ in range(n):
        lines.append(list(map(int, input().split())))
    lines.sort(key=lambda x: x[0])
    result = []
    cur = lines[0]
    for i in range(1, n):
        if lines[i][0] <= cur[1]:
            cur[1] = max(cur[1], lines[i][1])
        else:
            result.append(cur)
            cur = lines[i]
    result.append(cur)
    for line in result:
        print(line[0], line[1])
