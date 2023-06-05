def main():
    h, w = map(int, input().split())
    s = [input() for i in range(h)]
    print(sum([s[i].count("#") for i in range(h)]))
