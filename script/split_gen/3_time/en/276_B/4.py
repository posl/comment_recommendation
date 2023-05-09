def main():
    n, m = map(int, input().split())
    roads = []
    for i in range(m):
        roads.append(list(map(int, input().split())))
    roads.sort()
    for i in range(n):
        cnt = 0
        for j in range(m):
            if roads[j][0] == i+1:
                cnt += 1
            elif roads[j][1] == i+1:
                cnt += 1
        print(cnt)
