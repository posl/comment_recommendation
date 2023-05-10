def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [i for i in range(1, n + 1)]
    d = list(zip(a, b, c))
    d.sort(key=lambda x: x[2], reverse=True)
    d.sort(key=lambda x: x[1], reverse=True)
    d.sort(key=lambda x: x[0], reverse=True)
    print(*[i[2] for i in d[:x]], sep="\n")
