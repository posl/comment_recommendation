def main():
    n, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x:x[0])
    for a, b in ab:
        if k < a:
            break
        k += b
    print(k)
