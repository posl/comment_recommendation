def main():
    N, K = map(int, input().split())
    d = {}
    for i in range(1, K+1):
        d[i] = list(map(int, input().split()[1:]))
    count = 0
    for i in range(1, N+1):
        if i not in d.values():
            count += 1
    print(count)
