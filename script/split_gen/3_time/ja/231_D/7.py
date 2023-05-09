def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    left = 0
    right = 0
    for a, b in AB:
        if left < a:
            left = a
        if b <= right:
            continue
        if b - left > 1:
            print('No')
            return
        right = b
    print('Yes')
