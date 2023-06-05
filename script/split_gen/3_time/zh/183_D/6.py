def main():
    n, w = map(int, input().split())
    t = [0] * 200001
    for _ in range(n):
        s, e, p = map(int, input().split())
        t[s] += p
        t[e] -= p
    for i in range(1, 200001):
        t[i] += t[i-1]
        if t[i] > w:
            print('No')
            return
    print('Yes')
