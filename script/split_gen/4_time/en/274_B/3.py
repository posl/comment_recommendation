def main():
    H, W = map(int, input().split())
    C = [input() for i in range(H)]
    for i in range(W):
        print(sum([1 for j in range(H) if C[j][i] == '#']))
