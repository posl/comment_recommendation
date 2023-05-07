def main():
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        a, b = map(int, input().split())
        roads.append((a, b))
    roads.sort()
    prev = 1
    cnt = 0
    ans = []
    for a, b in roads:
        if a != prev:
            ans.append([cnt] + [i for i in range(prev, a)])
            prev = a
            cnt = 0
        cnt += 1
    ans.append([cnt] + [i for i in range(prev, n + 1)])
    for a in ans:
        print(' '.join(map(str, a)))
