def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    minA = min([min(a) for a in A])
    print(sum([sum([a-minA for a in ai]) for ai in A]))
