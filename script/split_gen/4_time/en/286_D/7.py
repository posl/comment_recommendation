def main():
    from sys import stdin
    readline = stdin.readline
    N, X = map(int, readline().split())
    AB = [tuple(map(int, readline().split())) for _ in range(N)]
    ans = 'No'
    for i in range(1, 2**N):
        total = 0
        for j in range(N):
            if i & (1 << j):
                total += AB[j][0] * AB[j][1]
        if total == X:
            ans = 'Yes'
            break
    print(ans)
