def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    min_A = min([min(i) for i in A])
    print(sum([sum([i - min_A for i in j]) for j in A]))
