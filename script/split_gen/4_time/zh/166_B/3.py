def main():
    n, k = map(int, input().split())
    d = []
    for i in range(k):
        d.append(list(map(int, input().split()))[1:])
    print(n - len(set(sum(d, []))))
