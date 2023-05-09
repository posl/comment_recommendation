def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    print(count(h, w, r, c))
