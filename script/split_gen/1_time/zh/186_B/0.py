def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    min_v = min([min(a) for a in A])
    print(sum([sum([a - min_v for a in a]) for a in A]))
