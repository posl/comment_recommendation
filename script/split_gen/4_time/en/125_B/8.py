def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    print(sum([a - b for a, b in zip(V, C) if a > b]))
