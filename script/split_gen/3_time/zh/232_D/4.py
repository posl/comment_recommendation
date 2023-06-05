def main():
    h, w = map(int, input().split())
    c = [input() for i in range(h)]
    print(walk(h, w, c))
