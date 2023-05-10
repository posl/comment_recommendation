def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in range(k):
        a.append(a.pop(0))
    print(' '.join([str(x) for x in a]))
