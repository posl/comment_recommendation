def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    visit = [0 for i in range(n+1)]
    visit[x] = 1
    count = 1
    while True:
        x = a[x]
        if visit[x] == 1:
            break
        else:
            visit[x] = 1
            count += 1
    print(count)
