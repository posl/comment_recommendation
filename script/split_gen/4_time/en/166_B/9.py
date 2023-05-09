def main():
    n, k = map(int, input().split())
    d = [0 for i in range(n)]
    for i in range(k):
        di = int(input())
        d = [d[j] + 1 if j+1 in map(int, input().split()) else d[j] for j in range(n)]
    print(d.count(0))
