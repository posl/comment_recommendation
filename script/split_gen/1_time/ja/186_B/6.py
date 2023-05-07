def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    A = [A_i for A_i in A for _ in range(W)]
    print(sum([min(A_i) for A_i in A]))
