def solution():
    n, k = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])
    for a, b in ab:
        if a > k:
            break
        k += b
    print(k)

if __name__ == '__main__':
    solution()