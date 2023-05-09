def main():
    n = int(input())
    h = list(map(int, input().split()))
    max_h = max(h)
    print(h.index(max_h) + 1)
