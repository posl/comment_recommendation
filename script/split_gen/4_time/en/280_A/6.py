def main():
    h, w = map(int, input().split())
    print(sum([s.count('#') for s in [input() for _ in range(h)]]))
