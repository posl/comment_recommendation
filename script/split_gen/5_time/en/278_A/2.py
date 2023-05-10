def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in range(k):
        a.pop(0)
        a.append(0)
    print(' '.join(map(str, a)))
