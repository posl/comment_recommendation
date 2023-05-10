def main():
    h, w = map(int, input().split())
    c = [input() for i in range(h)]
    for i in range(w):
        print(sum([1 for j in range(h) if c[j][i] == '#']))
