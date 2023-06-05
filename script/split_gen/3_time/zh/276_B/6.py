def main():
    n, m = map(int, input().split())
    city = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        city[a-1].append(b)
        city[b-1].append(a)
    for i in range(n):
        print(len(city[i]), *sorted(city[i]))
